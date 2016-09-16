from uber.common import *
from uber._version import __version__

if float(__version__) > 2014.09:
    # magfest 8.5 compatibility
    config = parse_config(__file__)

if float(__version__) > 2015.01:
    # didn't have 'c' object yet
    c.include_plugin_config(config)
