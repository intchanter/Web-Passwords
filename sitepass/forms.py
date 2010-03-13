from django import forms

class JoomlaForm(forms.Form):
    password = forms.CharField()

class OSCommerceForm(forms.Form):
    password = forms.CharField()
