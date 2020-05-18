import logging
import time
import math

import grpc

DEFAULT_OPTIONS = {
    "min_delay": 1,
    "max_delay": 50,
    "delay_factor": math.exp(1),
    "max_retries": 5
}
RETRY_CODES = [1, 2, 4, 10, 13, 14, 15]


class AuthenticatedService(object):
    """Initialization class for gRPC services.

    """
    def __init__(self, auth_token_func, stub, verbose=False, options=None):
        self.stub = stub
        self.auth_token_func = auth_token_func
        self.verbose = verbose
        if options:
            self.min_delay, self.max_delay, self.delay_factor, self.max_retries = self.parse_options(options)
        else:
            self.min_delay, self.max_delay, self.delay_factor, self.max_retries = 1, 50, math.exp(1), 5
        for method_name in dir(stub):
            method = getattr(stub, method_name)
            if not method_name.startswith('__') and callable(method):
                setattr(self, method_name, self.__decorated(method_name, method))

    def __decorated(self, method_name, method):
        def inner(param):
            auth_token = self.auth_token_func()
            if self.verbose:
                logging.info('Calling %s with token=`%s`' % (method_name, auth_token))
            if auth_token is not None:
                metadata = (('x-auth-ticket', auth_token),)
            else:
                metadata = None
            tries = 0
            delay = self.min_delay
            while 1:
                try:
                    return method(param, metadata=metadata)
                except grpc.RpcError as e:
                    if e._state.code.value[0] not in RETRY_CODES:
                        logging.error("Failed request to server, with error: " + e.details(), e.debug_error_string())
                        raise e
                    if self.max_retries > tries:
                        time.sleep(delay)
                        tries += 1
                        delay = min(delay * self.delay_factor, self.max_delay)
                        logging.error(str(e))
                        continue
                    logging.error("Max retries requests to server, with error: " + e.details(), e.debug_error_string())
                    raise e
        return inner

    @staticmethod
    def parse_options(options):
        for option, value in DEFAULT_OPTIONS.items():
            if option not in options:
                options[option] = value
        return options["min_delay"], options["max_delay"], options["delay_factor"], options["max_retries"]
