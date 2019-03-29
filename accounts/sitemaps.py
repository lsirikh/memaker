from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticAccountsSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return [
            'index',
            'login',
            'logout',
            'withdrawal',
            'withdrawal_done',
            'register',
            'account_activation_sent',
            'profile',
            'edit_profile',
            'find_id',
            'password_change',
            'password_change_done',
            'password_reset',
            'password_reset_done',
            'password_reset_complete',
                ]

    def location(self, item):
        return reverse('accounts:'+item)

