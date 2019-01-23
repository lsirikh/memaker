from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)