from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from products.models import Category, Content, Appraisal, Video

class StaticProductsSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return ['product_list', 'lecture_list']

    def location(self, item):

        return reverse('products:'+item)

class CategorySitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def location(self, item):
        return reverse('products:content_category_list', args=[item.slug])

class ContentSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return Content.objects.all()

    def location(self, item):
        return reverse('products:content_information', args=[item.slug])

class VideoSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return Video.objects.all()

    def location(self, item):
        return reverse('products:content_video', args=[item.lecture.content.slug, item.pk])

class AppraisalSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Content.objects.all()

    def location(self, item):
        return reverse('products:content_review', args=[item.slug])