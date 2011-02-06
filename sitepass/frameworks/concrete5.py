from hashlib import md5

name = 'Concrete5'
url = 'concrete5'
title = 'Generate %s Password Hash' % name

help_text = '''
<p>Enter your desired password in the Password field, then fill the Salt field
using the information from the config/site.php file in your Concrete5
installation.  Be sure to grab the whole salt value, without the enclosing
quote marks.</p>
<p>After you submit the form, you will be provided with the database entry,
which you can set directly in the database.</p>
'''

from sitepass.forms import Concrete5Form as form_class

def hash(form):
    password = form.cleaned_data['password']
    salt = form.cleaned_data['salt']
    return md5(password + ':' + salt).hexdigest()
