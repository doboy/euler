from django.conf.urls.defaults import patterns, include, url
from euler.views import home, add

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', home),
                       (r'^add/$', add),
    # Examples:
    #  url(r'^$', 'euler.views.home', name='home'),
    # url(r'^euler/', include('euler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
