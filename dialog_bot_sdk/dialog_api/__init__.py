import six
PATH_WORKAROUND = six.PY3

if PATH_WORKAROUND:
    import sys
    import os
    sys.path.append(os.path.dirname(__file__))

