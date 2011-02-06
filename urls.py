from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^style/', include('passwordsoup.styles.urls')),
    (r'^hash/', include('passwordsoup.sitepass.urls')),
    (r'^articles/', include('articles.urls')),

    (r'^admin/', include(admin.site.urls)),
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/webalizer/', include('webalizer.urls')),

    (r'', include('passwordsoup.home.urls')),
)
