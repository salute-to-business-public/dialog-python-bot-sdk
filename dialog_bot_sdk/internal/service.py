import time
import math
import traceback
import uuid
import grpc
from dialog_bot_sdk.utils import build_error_string, build_log_string


DEFAULT_OPTIONS_RETRY = {
    "min_delay": 1,
    "max_delay": 50,
    "delay_factor": math.exp(1),
    "max_retries": 10
}
RETRY_CODES = [1, 2, 4, 10, 13, 14, 15]


class AuthenticatedService(object):
    """Initialization class for gRPC services.

    """
    def __init__(self, auth_token_func: callable, stub, **kwargs):
        self.stub = stub
        self.auth_token_func = auth_token_func
        self.verbose = kwargs.get("verbose")
        self.rate_limiter = kwargs.get("rate_limiter")
        self.retry_options = kwargs.get("retry_options")
        self.timeout = kwargs.get("timeout")
        self._logger = kwargs["logger"]

        for method_name in dir(stub):
            method = getattr(stub, method_name)
            if not method_name.startswith('__') and callable(method):
                setattr(self, method_name, self.__decorated(method_name, method))

    def __decorated(self, method_name, method):
        def inner(param):
            auth_token = self.auth_token_func()
            if auth_token is not None:
                metadata = (('x-auth-ticket', auth_token),)
            else:
                metadata = None
            tries = 0
            delay = self.retry_options["min_delay"]
            request_uuid = str(uuid.uuid4())
            while 1:
                try:
                    with self.rate_limiter:
                        self._logger.debug(
                            build_log_string(
                                request_uuid=request_uuid, method=method_name, request=param, timeout=self.timeout
                            )
                        )

                        result = method(
                            param,
                            metadata=metadata,
                            timeout=self.timeout,
                        )

                        self._logger.debug(build_log_string(request_uuid=request_uuid, response=result))

                        return result
                except grpc.RpcError as e:
                    if e._state.code.value[0] not in RETRY_CODES:
                        self._logger.error(
                            build_error_string(
                                e, request_uuid=request_uuid, method_name=method_name, request=param,
                                traceback=traceback.format_exc()
                            )
                        )
                        raise e
                    tries, delay = self.retry(tries, delay, e, request_uuid, method_name, param)

        return inner

    def retry(self, tries: int, delay: float, e: grpc.RpcError, request_uuid: str, method_name: str, request):
        if self.retry_options["max_retries"] > tries:
            self._logger.error(
                build_error_string(
                    e, retry=tries + 1, max_retries=self.retry_options["max_retries"], request_uuid=request_uuid,
                    method=method_name
                )
            )
            time.sleep(delay)
            tries += 1
            delay = min(delay * self.retry_options["delay_factor"], self.retry_options["max_delay"])
            return tries, delay
        self._logger.error(
            build_error_string(
                e, request_uuid=request_uuid, method=method_name, request=request,
                annotation="Max retries requests to server", traceback=traceback.format_exc()
            )
        )
        raise e
