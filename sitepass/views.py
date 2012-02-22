# Create your views here.

from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import Http404
from frameworks import *
#import frameworks

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
    #print framework_link.keys()
    frameworks = framework_link.keys()
    frameworks.sort()
    data = (
        #framework,
        {
            'name': framework_link[framework].name,
            'url': framework_link[framework].url,
        }
        for framework in frameworks
    )
    return render_to_string('menu.html', {'items': data})

def sitepass(request, framework):
    hash = None
    error = None
    try:
        pieces = framework_link[framework]
    except KeyError:
        raise Http404
    if request.method == 'POST':
        form = pieces.form_class(request.POST)
        if form.is_valid():
            try:
                hash = pieces.hash(form)
            except UnicodeEncodeError:
                error = 'For the purposes of this form, only enter plain ASCII passwords.'
    else:
        form = pieces.form_class()
    fillers = {
        'title': pieces.title,
        'hash': hash,
        'form': form,
        'error': error,
        'help_text': pieces.help_text,
        'menu': menu(request),
    }
    return render_to_response('sitepass.html', fillers)
