from django import forms

class BasicForm(forms.Form):
    password = forms.CharField()

class JoomlaForm(BasicForm):
    pass

class OSCommerceForm(BasicForm):
    pass

class ZenCartForm(BasicForm):
    pass

class Concrete5Form(BasicForm):
    salt = forms.CharField()
