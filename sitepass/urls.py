from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^joomla/$', joomla),
    (r'^oscommerce/$', oscommerce),
    (r'^concrete5/$', concrete5),
)
