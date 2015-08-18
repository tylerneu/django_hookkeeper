import os, sys, re

proj_path = "/Users/tyler.neu/Code/django_hookkeeper"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_hookkeeper.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from pulls.models import Klass

f = open(proj_path + '/scripts/ITPA_classes.txt', 'r')
for line in f:
    m = re.match(r"(\d+) (.+)", line)
    k = Klass(weight = m.groups()[0] , name = m.groups()[1])
    print k
    k.save()
