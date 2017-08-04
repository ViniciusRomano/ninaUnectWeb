from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^entrada/(?P<ra>[0-9]+)/(?P<empresa>[0-9]+)/$', views.entrada, name='entrada'),
    url(r'^saida/(?P<ra>[0-9]+)/(?P<empresa>[0-9]+)/$', views.saida, name='saida'),
]