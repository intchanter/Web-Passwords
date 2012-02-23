from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hash/', include('sitepass.urls')),
    (r'^articles/', include('articles.urls')),

    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/webalizer/', include('webalizer.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'', include('home.urls')),
)
