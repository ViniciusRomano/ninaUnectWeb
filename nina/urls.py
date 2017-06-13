from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

admin.site.site_header = 'Nina'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^permanencia/', include('permanencia.urls')),
    url(r'^relatorio/', include('relatorio.urls')),
    url(r'^', include('hello.urls')),
]
