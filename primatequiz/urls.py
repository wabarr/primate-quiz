from django.conf.urls import patterns, url
from primatequiz.views import *
from django.conf.urls.static import static



urlpatterns = patterns('',
        url(r'$^', quiz),
        url(r'results/(?P<slug>.+)$',results),
        url(r'results/$',results),
        )


