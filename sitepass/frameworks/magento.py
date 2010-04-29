from sitepass.randstring import randstring, alphanum
from sitepass.forms import MagentoForm
from hashlib import md5

title = 'Generate Magento Password Hash'

help_text = '''<p>help_text</p>'''

form_class = MagentoForm

def hash(form):
    password = form.cleaned_data['password']
    salt = randstring(alphanum, 2)
    return md5(salt + password).hexdigest() + ':' + salt
