from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticIntroSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse('intro:'+item)