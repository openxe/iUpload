from django.conf import settings
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^storage/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^$', 'iupload.views.index', name='home'),
    url(r'^upload$', 'iupload.views.upload', name='upload'),
    url(r'^upload_success$', 'iupload.views.upload', {'uploaded': True,}, name='upload_success'),
    url(r'^resize/(?P<width>\d+)/(?P<height>\d+)/(?P<path>.*)$', 'iupload.views.resize', name='resize'),
)
