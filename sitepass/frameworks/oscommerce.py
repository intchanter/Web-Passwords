from sitepass.randstring import randstring, alphanum
from hashlib import md5

title = 'Generate OSCommerce Password Hash'

help_text = '''<p>help_text</p>'''

from sitepass.forms import OSCommerceForm as form_class

def hash(form):
    password = form.cleaned_data['password']
    salt = randstring(alphanum, 2)
    return md5(salt + password).hexdigest() + ':' + salt
