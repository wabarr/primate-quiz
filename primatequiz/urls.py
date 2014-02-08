from django.conf.urls import patterns, url
from primatequiz.views import *
from django.conf.urls.static import static
from base import settings


urlpatterns = patterns('',
        url(r'$^', quiz),
        url(r'results/(?P<slug>.+)$',results),
        url(r'results/$',results),
        )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
