from sitepass.randstring import randstring, alphanum
from hashlib import md5

title = 'Generate Joomla Password Hash'

help_text = '''<p>help_text</p>'''

from sitepass.forms import JoomlaForm as form_class

def hash(form):
    password = form.cleaned_data['password']
    salt = randstring(alphanum, 32)
    return md5(password + salt).hexdigest() + ':' + salt
