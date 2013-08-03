from django.conf import settings
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^$', 'iupload.views.index', name='home'),
    url(r'^upload$', 'iupload.views.upload', name='upload'),
)
