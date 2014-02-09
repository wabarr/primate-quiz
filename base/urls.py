from django.conf.urls import patterns, include, url
from primatequiz.views import *
from django.contrib import admin
admin.autodiscover()
from base import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^base/', renderBase, name="renderBase"),
    url(r'^primate_quiz/', include("primatequiz.urls"))
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))