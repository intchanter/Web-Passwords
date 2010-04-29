from sitepass.randstring import randstring, alphanum
from sitepass.forms import CubeCartForm
from hashlib import md5

title = "Generate CubeCart Password Hash"

help_text = '''<p>help_text</p>'''

form_class = CubeCartForm

def hash(form):
    salt = randstring(alphanum, 6)
    password = form.cleaned_data['password']
    salt_hash = md5(salt).hexdigest()
    pass_hash = md5(password).hexdigest()
    return md5(salt_hash + pass_hash).hexdigest()
