from sitepass.forms import DrupalForm
from hashlib import md5

title = 'Generate Drupal Password Hash'

help_text = '''<p>help_text</p>'''

form_class = DrupalForm

def hash(form):
    password = form.cleaned_data['password']
    return md5(password).hexdigest()
