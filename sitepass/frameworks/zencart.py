from sitepass.randstring import randstring, alphanum
from hashlib import md5

name = 'Zen Cart'
url = 'zencart'
title = 'Generate %s Password Hash' % name

help_text = '''<p>help_text</p>'''

from sitepass.forms import ZenCartForm as form_class

def hash(form):
    password = form.cleaned_data['password']
    salt = randstring(alphanum, 2)
    return md5(salt + password).hexdigest() + ':' + salt
