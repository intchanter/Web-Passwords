from django.conf.urls.defaults import *
from views import stylesheet

urlpatterns = patterns('',
    ('^$', stylesheet),
)
