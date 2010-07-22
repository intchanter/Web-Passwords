from django import forms

class BasicForm(forms.Form):
    password = forms.CharField()

class Concrete5Form(BasicForm):
    salt = forms.CharField()

class CubeCartForm(BasicForm):
    pass

class DrupalForm(BasicForm):
    pass

class JoomlaForm(BasicForm):
    pass

class MagentoForm(BasicForm):
    pass

class OSCommerceForm(BasicForm):
    pass

class ZenCartForm(BasicForm):
    pass

class ZenPhotoForm(BasicForm):
    user = forms.CharField()
    extra_auth_hash_text = forms.CharField(required=False)
