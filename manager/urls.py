from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('manager.views',
    url(r'^manager', 'manager', name="manager"),
    url(r'^createUser', 'create_user', name="create_user"),
    url(r'^checkSales', 'check_sales', name="check_sales"),


)
