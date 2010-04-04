# Create your views here.

from django.shortcuts import render_to_response
from hashlib import md5
from random import choice
import string
import forms

def randstring(charset, length):
    chars = []
    for x in range(length):
        chars.append(choice(charset))
    return ''.join(chars)

def oscommerce(request):
    hash = None
    form = forms.OSCommerceForm()
    if request.method == 'POST':
        form = forms.OSCommerceForm(request.POST)
        if form.is_valid():
            password = string.strip(request.POST['password'])
            salt = randstring(string.ascii_letters + string.digits, 2)
            hash = md5(salt + password).hexdigest() + ':' + salt
    return render_to_response('sitepass.html', {'title': 'osCommerce Password Generation Utility', 'hash': hash, 'form': form})

def joomla(request):
    hash = None
    form = forms.JoomlaForm()
    if request.method == 'POST':
        form = forms.JoomlaForm(request.POST)
        if form.is_valid():
            password = string.strip(request.POST['password'])
            salt = randstring(string.ascii_letters + string.digits, 32)
            hash = md5(password + salt).hexdigest() + ':' + salt
    return render_to_response('sitepass.html', {'title': 'Joomla Password Generation Utility', 'hash': hash, 'form': form})

def concrete5(request):
    hash = None
    form = forms.Concrete5Form()
    if request.method == 'POST':
        form = forms.Concrete5Form(request.POST)
        if form.is_valid():
            password = string.strip(request.POST['password'])
            salt = string.strip(request.POST['salt'])
            hash = md5(password + ':' + salt).hexdigest()
    return render_to_response('sitepass.html', {'title': 'Concrete5 Password Generation Utility', 'hash': hash, 'form': form})
