from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    ('^joomla/$', joomla),
    ('^oscommerce/$', oscommerce),
    ('^concrete5/$', concrete5),
    #('', .),
)
