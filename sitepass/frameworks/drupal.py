from hashlib import md5

title = 'Generate Drupal Password Hash'

help_text = '''<p>help_text</p>'''

from sitepass.forms import DrupalForm as form_class

def hash(form):
    password = form.cleaned_data['password']
    return md5(password).hexdigest()
