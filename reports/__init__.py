from uber.common import *
from ._version import __version__
from .config import *
from .models import *
from .model_checks import *
from .automated_emails import *

# magfest 8.5 compatibility
from uber._version import __version__
if float(__version__) > 2014.09:
    # TODO: we'll need to figure out how to do this stuff for mag8.5 which
    # is pre-sideboard. might still be easy.
    static_overrides(join(config['module_root'], 'static'))
    template_overrides(join(config['module_root'], 'templates'))
    mount_site_sections(config['module_root'])
