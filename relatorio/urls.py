from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<dia>[0-9]+)/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/$', views.dia, name='dia'),
    url(r'^hoje/$', views.hoje, name='hoje'),
    url(r'^(?P<ra>[0-9]+)/$', views.funcionario),
]