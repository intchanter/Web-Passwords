# Create your views here.

from django.shortcuts import render_to_response
from hashlib import md5
import string
import forms

def joomla(request):
    pass

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

def zencart(request):
    '''TODO: make this work the same as oscommerce(), but with the right
strings'''
    return oscommerce(request)

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

from frameworks import joomla

framework_link = {
    #'concrete5': concrete5,
    #'cubecart': cubecart,
    'joomla': joomla,
    #'oscommerce': oscommerce,
    #'zencart': zencart,
}

def sitepass(request, framework):
    hash = None
    pieces = framework_link[framework]
    if request.method == 'POST':
        form = pieces.form_class(request.POST)
        if form.is_valid():
            hash = pieces.hash(form)
    else:
        form = pieces.form_class()
    fillers = {
        'title': pieces.title,
        'hash': hash,
        'form': form,
        'help_text': pieces.help_text,
    }
    return render_to_response('sitepass.html', fillers)
