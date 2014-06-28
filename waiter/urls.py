from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('waiter.views',
    url(r'^waiter', 'waiter', name="waiter"),

)
