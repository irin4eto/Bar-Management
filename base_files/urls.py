from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'', include('users.urls', namespace='users')),

    url(r'', include('website.urls', namespace='website')),

    url(r'', include('manager.urls', namespace='manager')),

    url(r'', include('waiter.urls', namespace='waiter')),

    url(r'', include('bartender.urls', namespace='bartender')),

    url(r'^admin/', include(admin.site.urls)),
)
