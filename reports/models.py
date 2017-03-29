from uber.common import *
from uber._version import __version__


def get_all_models():
    if float(__version__) > 2014.09:
        # normal mode
        return Session.all_models()
    else:
        # magfest 8.5 compatibility mode
        return all_models()
