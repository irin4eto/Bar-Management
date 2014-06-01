from django.conf.urls import patterns
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = patterns('users.views',
    url(r'^login/$', 'user_login', name="user_login"),
    url(r'^manager', 'manager', name="manager"),
    url(r'^createUser', 'create_user', name="create_user"),
    url(r'^manager/$', RedirectView.as_view(url=reverse_lazy('create_user')), name='manager'),

)

