from sitepass.randstring import randstring, alphanum
from hashlib import md5

name = 'Zen Photo'
url = 'zenphoto'
title = 'Generate %s Password Hash' % name

help_text = '''<p>help_text</p>'''

from sitepass.forms import ZenPhotoForm as form_class

# Note that the framework itself does some stricter checking when setting
# passwords to ensure site-specific length requirements and such are met.
# For simplicity, we're not doing that here, but we'll recommend that users
# change their passwords immediately after successfully logging in.
def hash(form):
    salt = randstring(alphanum, 6)
    user = form.cleaned_data['user']
    password = form.cleaned_data['password']
    extra_auth_hash_text = form.cleaned_data['extra_auth_hash_text']
    pass_hash = md5(user + password + extra_auth_hash_text).hexdigest()
    return pass_hash
