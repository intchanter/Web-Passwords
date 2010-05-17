from sitepass.randstring import randstring, alphanum
from hashlib import md5

title = 'Generate OSCommerce Password Hash'

help_text = '''<p>help_text</p>'''

from sitepass.forms import OSCommerceForm as form_class

# This algorithm appears to defeat the purpose of salt by guaranteeing
# that the same database entry will always be generated for a given
# password.  Assuming it is shown to work, prefer a random salt over
# purity.
def hash(form):
    password = form.cleaned_data['password']
    temp = md5(password).hexdigest()
    #salt = randstring(alphanum, 2)
    salt = temp[0:2]
    return md5(salt + password).hexdigest() + ':' + salt
