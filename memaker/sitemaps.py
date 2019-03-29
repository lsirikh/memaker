from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

import logging
logger = logging.getLogger('sitemapLogger')

class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)