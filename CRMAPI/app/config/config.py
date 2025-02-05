
import os

if os.environ.get('ENV') == 'dev':
    from .config_dev import *
else:
    from .config_local import *
