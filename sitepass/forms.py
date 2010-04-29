from django import forms

class BasicForm(forms.Form):
    password = forms.CharField()

class Concrete5Form(BasicForm):
    salt = forms.CharField()

class CubeCartForm(BasicForm):
    pass

class JoomlaForm(BasicForm):
    pass

class OSCommerceForm(BasicForm):
    pass

class ZenCartForm(BasicForm):
    pass
