from spitfire import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spitfire.views.home', name='home'),
    # url(r'^spitfire/', include('spitfire.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^other/', views.other, name='other'),
    url(r'^admin/', include(admin.site.urls)),
)
