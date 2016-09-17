from uber.common import *
from ._version import __version__
from .config import *
from .models import *
from .model_checks import *
from .automated_emails import *

from uber._version import __version__

if float(__version__) > 2014.09:
    # anything beyond magfest 8.5 can access this normally
    module_root = config['module_root']
else:
    # magfest 8.5 doesn't have new-style config stuff, so fake it.
    # new code should NEVER get here.
    module_root = '/usr/local/uber85/plugins/reports/reports'

if float(__version__) >= 2014.09:
    static_overrides(join(module_root, 'static'))
    template_overrides(join(module_root, 'templates'))
    mount_site_sections(module_root)
