# Create your views here.

from django.shortcuts import render_to_response
from hashlib import md5
from random import choice
import string

def randstring(charset, length):
    chars = []
    for x in range(length):
        chars.append(choice(charset))
    return ''.join(chars)

def joomla(request):
    hash = ''
    error = ''
    ok = True
    if request.method == 'POST':
        # Check form data
        if request.POST['submit'] != 'Generate!':
	    error = 'This form may only be accessed from this page.'
	    ok = False
	password = string.strip(request.POST['password'])
	if password == '':
	    error = 'Please specify a password to use.'
	    ok = False
        # Handle form data
	if ok:
	    salt = randstring(string.ascii_letters + string.digits, 32)
	    hash = md5(password + salt).hexdigest() + ':' + salt
    return render_to_response('joomla.html', {'title': 'Joomla Password Generation Utility', 'hash': hash, 'error': error})

def concrete5(request):
    if request.method == 'POST':
        # Check form data
	# Handle form data
	pass
    return render_to_response()
