# Create your views here.

from django.shortcuts import render_to_response
from django.http import Http404
from frameworks import *

framework_link = {
    'concrete5': concrete5,
    'cubecart': cubecart,
    'drupal': drupal,
    'joomla': joomla,
    'magento': magento,
    'oscommerce': oscommerce,
    'zencart': zencart,
    'zenphoto': zenphoto,
}

def menu(request):
    print framework_link.keys()
    frameworks = framework_link.sort()
    data = (
        #framework,
        {
            'name': framework_link[framework].name,
            'url': framework_link[framework].url,
        }
        for framework in frameworks
    )
    return render_to_response('menu.html', {'items': data})

def sitepass(request, framework):
    hash = None
    try:
        pieces = framework_link[framework]
    except KeyError:
        raise Http404
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
