from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('users.views',
    url(r'^login/$', 'user_login', name="user_login"),

)

