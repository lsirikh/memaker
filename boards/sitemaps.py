from django.contrib.sitemaps import Sitemap
from boards.models import Board, Topic
from django.shortcuts import reverse

class StaticBoardsSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse('boards:'+item)

class BoardSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return Board.objects.all()

    def location(self, item):
        return reverse('boards:board_topic', args=[item.pk])

class TopicSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return Topic.objects.all()

    def location(self, item):
        return reverse('boards:board_topic', args=[item.pk])
