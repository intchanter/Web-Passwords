from hashlib import md5

name = 'Drupal'
url = 'drupal'
title = 'Generate %s Password Hash' % name

help_text = '''<p>help_text</p>'''

from sitepass.forms import DrupalForm as form_class

def hash(form):
    password = form.cleaned_data['password']
    return md5(password).hexdigest()
