from django import forms

class JoomlaForm(forms.Form):
    password = forms.CharField()
