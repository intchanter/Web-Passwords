# Create your views here.

from django.shortcuts import render_to_response
from frameworks import joomla, oscommerce, zencart, concrete5, cubecart

framework_link = {
    'concrete5': concrete5,
    'cubecart': cubecart,
    'joomla': joomla,
    'oscommerce': oscommerce,
    'zencart': zencart,
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
