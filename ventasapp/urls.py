from django.conf.urls import patterns, include, url
from django.contrib import admin
from ventasapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^salesSimulation/$', views.simulation , name="simulation"),
    url(r'^sales/$',views.list_sales, name="list_sales"),
    url(r'^sales/(?P<sale>([0-9]{1,9}))/$', views.show_sale),
    url(r'^sales/create/$', views.create_sale),
    url(r'^sales/(?P<sale>([0-9]{1,9}))/edit/$', views.edit_sale),
    url(r'^sales/(?P<sale>([0-9]{1,9}))/delete/$', views.delete_sale),
	#url(r'^search/$', views.search, name='search'),
	url(r'^salesSimulation/create/$', views.create_item),
	url(r'^salesSimulation/(?P<item>([0-9]{1,9}))/edit/$', views.edit_item),
	url(r'^salesSimulation/(?P<item>([0-9]{1,9}))/delete/$', views.delete_item),
    url(r'^(?P<cashier>([0-9]{1,9}))/edit_settings/$', views.edit_settings),
)