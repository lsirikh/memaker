"""memaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from memaker import views  # add for landingpage
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ckeditor_uploader.urls import views as uploader_views

from django.contrib.sitemaps.views import sitemap
from accounts.sitemaps import StaticAccountsSitemap
from boards.sitemaps import StaticBoardsSitemap, BoardSitemap, TopicSitemap
from products.sitemaps import (
    StaticProductsSitemap,
    CategorySitemap,
    ContentSitemap,
    VideoSitemap,
    AppraisalSitemap
)

from intro.sitemaps import StaticIntroSitemap
from memaker.sitemaps import StaticSitemap

sitemaps = {
    'static': StaticSitemap,
    'static_intro': StaticIntroSitemap,
    'static_accounts': StaticAccountsSitemap,
    'static_products': StaticProductsSitemap,
    'static_boards': StaticBoardsSitemap,
    'board': BoardSitemap,
    'topic': TopicSitemap,
    'category': CategorySitemap,
    'content': ContentSitemap,
    'video': VideoSitemap,
    'appraisal': AppraisalSitemap,
}

app_name = 'memaker'
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('_nested_admin/', include('nested_admin.urls')),

                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  # path('ckeditor/upload/', uploader_views.upload, name='ckeditor_upload'),
                  # path('ckeditor/browse/', uploader_views.browse, name='ckeditor_browse'),

                  #    re_path(r'^r/$', views.login_redirect, name='login_redirect'),
                  path('', views.HomeView.as_view(), name='home'),
                  path('google2cea96b33d0c202f.html/', views.GoogleView.as_view()),
                  path('google640e077116d2555d.html/', views.GoogleView2nd.as_view()),
                  path('navere8566efa5b506b61efd740303a95e363.html/', views.NaverView.as_view()),
                  path('robots.txt/', views.NaverRobot.as_view()),
                  path('polls/', include('polls.urls')),
                  path('intro/', include('intro.urls')),
                  path('products/', include('products.urls')),
                  path('lectures/', include('lectures.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('boards/', include('boards.urls')),
                  path('cart/', include('cart.urls', namespace='cart')),
                  path('orders/', include('orders.urls', namespace='orders')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
