from uber.common import *
from ._version import __version__
from .config import *
from .models import *
from .model_checks import *
from .automated_emails import *

from uber._version import __version__
if float(__version__) >= 2014.09:
    static_overrides(join(config['module_root'], 'static'))
    template_overrides(join(config['module_root'], 'templates'))
    mount_site_sections(config['module_root'])
