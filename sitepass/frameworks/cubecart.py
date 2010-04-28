from randstring import randstring
from hashlib import md5

class CubeCart(Object):
    def __init__(self):
        pass

    def hash(self, bound_form):
        salt = randstring(6)
        password = bound_form.password
        salt_hash = md5(salt).hexdigest()
        pass_hash = md5(password).hexdigest()
        return md5(salt_hash + pass_hash).hexdigest()

    def form(self):
        pass
