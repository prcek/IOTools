import sys
import os

app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, app_dir)

activate_this = os.path.join(app_dir,  '.venv/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

from hello import app
from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(app, True)
