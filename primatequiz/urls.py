from django.conf.urls import patterns, url
from primatequiz.views import *
from django.conf.urls.static import static
from primatequiz.sitemap.sitemap import sitemaps



urlpatterns = patterns('',
        url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
        url(r'$^', quiz),
        url(r'results/(?P<slug>.+)$',results),
        url(r'results/$',results),
        )


