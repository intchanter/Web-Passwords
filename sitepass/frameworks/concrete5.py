from sitepass.forms import Concrete5Form
from hashlib import md5

title = 'Generate Concrete5 Password Hash'

help_text = '''<p>help_text</p>'''

form_class = Concrete5Form

def hash(form):
    password = form.cleaned_data['password']
    salt = form.cleaned_data['salt']
    return md5(password + ':' + salt).hexdigest()
