from hashlib import md5

name = 'Concrete5'
url = 'concrete5'
title = 'Generate %s Password Hash' % name

help_text = '''<p>help_text</p>'''

from sitepass.forms import Concrete5Form as form_class

def hash(form):
    password = form.cleaned_data['password']
    salt = form.cleaned_data['salt']
    return md5(password + ':' + salt).hexdigest()
