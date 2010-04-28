from randstring import randstring
from hashlib import md5

title = "Generate a CubeCart Password Hash"

help_text = """
"""

def hash(self, bound_form):
    salt = randstring(6)
    password = bound_form.password
    salt_hash = md5(salt).hexdigest()
    pass_hash = md5(password).hexdigest()
    return md5(salt_hash + pass_hash).hexdigest()

def form(self):
    pass
