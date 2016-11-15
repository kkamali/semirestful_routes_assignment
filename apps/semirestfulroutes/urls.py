from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products$', views.index, name = "index"),
    url(r'products/(?P<product>\w+)/$', views.show, name = "show"),
    url(r'products/(?P<product>\w+)/edit/$', views.edit, name = "edit"),
    url(r'products/(?P<product>\w+)/remove$', views.remove, name = "remove"),
    url(r'products/new$', views.add, name = "new"),
    url(r'products/create$', views.create, name = "create"),
    url(r'products/(?P<product>\w+)/update$', views.update, name = "update")
]
