from django.conf.urls.defaults import *
from views import joomla
from views import oscommerce

urlpatterns = patterns('',
    ('^joomla/$', joomla),
    ('^oscommerce/$', oscommerce),
    #('', ''),
)
