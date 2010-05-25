from sitepass.randstring import randstring, alphanum
from hashlib import md5

name = 'CubeCart'
url = 'cubecart'
title = 'Generate %s Password Hash' % name

help_text = '''<p>help_text</p>'''

from sitepass.forms import CubeCartForm as form_class

def hash(form):
    salt = randstring(alphanum, 6)
    password = form.cleaned_data['password']
    salt_hash = md5(salt).hexdigest()
    pass_hash = md5(password).hexdigest()
    return md5(salt_hash + pass_hash).hexdigest()
