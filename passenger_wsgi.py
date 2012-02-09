import os, sys

INTERP = "/usr/bin/python2.6"
# INTERP is present twice so that the new python interpreter knows the
# actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)


# Path to the directory from which Django can be imported
#sys.path.append('/home7/intchant/.local/lib/python-2.6/site-packages')
# Path to the directory from which apps can be imported
sys.path.append('/var/www/passwordsoup')
# Path to the directory from which my app can be imported
sys.path.append('/var/www')

os.environ['DJANGO_SETTINGS_MODULE'] = 'passwordsoup.settings'

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()

