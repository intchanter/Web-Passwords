from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^$', menu),
    (r'^(?P<framework>\w+)/$', sitepass),
)
