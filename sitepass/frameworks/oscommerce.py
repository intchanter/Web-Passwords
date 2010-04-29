from sitepass.randstring import randstring, alphanum
from sitepass.forms import OSCommerceForm
from hashlib import md5

title = 'Generate OSCommerce Password Hash'

help_text = '''<p>help_text</p>'''

form_class = OSCommerceForm

def hash(form):
    password = form.cleaned_data['password']
    salt = randstring(alphanum, 2)
    return md5(salt + password).hexdigest() + ':' + salt


def aoeuoscommerce(request):
    hash = None
    form = forms.OSCommerceForm()
    if request.method == 'POST':
        form = forms.OSCommerceForm(request.POST)
        if form.is_valid():
            password = string.strip(request.POST['password'])
            salt = randstring(string.ascii_letters + string.digits, 2)
            hash = md5(salt + password).hexdigest() + ':' + salt
    return render_to_response('sitepass.html', {'title': 'osCommerce Password Generation Utility', 'hash': hash, 'form': form})
