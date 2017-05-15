from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^(?P<ra>[0-9]+)/(?P<dia>[0-9]+)/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/$', hello.views.permanencias),
    url(r'^(?P<dia>[0-9]+)/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/$', hello.views.dia),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entrada/(?P<ra>[0-9]+)/$', hello.views.entrada),
    url(r'^saida/(?P<ra>[0-9]+)/$', hello.views.saida),
    url(r'^hoje/', hello.views.hoje),
]
