from sitepass.randstring import randstring, alphanum
from sitepass.forms import OSCommerceForm
from hashlib import md5

title = 'Generate OSCommerce Password Hash'

help_text = '''<p>help_text</p>'''

form_class = OSCommerceForm

def hash(form):
    password = form.cleaned_data['password']
    salt = randstring(alphanum, 2)
    return md5(salt + password).hexdigest() + ':' + salt
