from sitepass.randstring import randstring, alphanum
from sitepass.forms import ZenCartForm
from hashlib import md5

title = 'Generate Zen Cart Password Hash'

help_text = '''<p>help_text</p>'''

form_class = ZenCartForm

def hash(form):
    password = form.cleaned_data['password']
    salt = randstring(alphanum, 2)
    return md5(salt + password).hexdigest() + ':' + salt
