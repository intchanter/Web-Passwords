from django.conf.urls.defaults import *
from views import joomla

urlpatterns = patterns('',
    ('^joomla/$', joomla),
    #('', ''),
)
