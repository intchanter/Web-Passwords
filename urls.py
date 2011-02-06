from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^style/', include('passwordsoup.styles.urls')),
    (r'^hash/', include('passwordsoup.sitepass.urls')),
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^articles/', include('articles.urls')),
    (r'', include('passwordsoup.home.urls')),
)
