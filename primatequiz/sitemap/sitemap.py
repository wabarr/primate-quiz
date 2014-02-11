from django.contrib.sitemaps import Sitemap

# import your own data structures here
from primatequiz.models import species


class BasicSitemap(Sitemap):
    priority = 0.5
    lastmod = None

    def items(self):
        return [
                "/",
            ]

    def location(self, obj):
        return obj

    def changefreq(self, obj):
        return "weekly"

class GenericDynamicSiteMap(Sitemap):
    priority = 0.5
    changefreq = "weekly"
    lastmod = None

    def location(self, obj):
        return obj.get_absolute_url()



class PrimateSiteMap(GenericDynamicSiteMap):

    def items(self):
        return species.objects.all()

sitemaps = dict(
        species = PrimateSiteMap,
        base = BasicSitemap,
        # ...
    )