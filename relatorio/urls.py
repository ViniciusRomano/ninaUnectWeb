from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<empresa>[0-9]+)/(?P<dia>[0-9]+)/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/$', views.dia, name='dia'),
    url(r'^(?P<empresa>[0-9]+)/hoje/$', views.hoje, name='hoje'),
    url(r'^(?P<empresa>[0-9]+)/(?P<ra>[0-9]+)/$', views.funcionario),
]