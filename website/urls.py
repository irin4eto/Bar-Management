from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('website.views',
    (r'^$', 'index'),
)

urlpatterns += staticfiles_urlpatterns()
