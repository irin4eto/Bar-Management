from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('bartender.views',
    url(r'^bartender/', 'bartender', name="bartender"),

)
