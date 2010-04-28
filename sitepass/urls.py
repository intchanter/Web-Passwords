from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^(?P<framework>\w+)/$', sitepass),
)
