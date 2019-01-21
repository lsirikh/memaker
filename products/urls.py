"""mysite URL Configuration

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
from products import views
from django.urls import path, re_path

app_name = 'products'
urlpatterns = [
    # path('', views.ProductModelView.as_view(), name='index'),
    # /products/product-list
    path('product-list/', views.ProductListView.as_view(),
         name='product_list'),
    # /products/lecture-list/
    path('lecture-list/', views.LectureListView.as_view(),
         name='lecture_list'),
    # /products/category-list/엔트리/
    # 한글로 slug:'엔트리' dispatch 에러 나타남
    # path('category-list/<str:category_slug>/', views.ContentCategoryListView.as_view(),
    #      name='content_category_list'),
    re_path('category-list/(?P<category_slug>[-\w]+)/$', views.ContentCategoryListView.as_view(),
         name='content_category_list'),

    # /products/content/미메이커-코딩보드/information
    # path('content/<int:pk>/information/', views.ContentInformationView.as_view(),
    #      name='content_information'),
    # re_path(r'^content/(?P<pk>[0-9]+)/information/$', views.ContentInformationView.as_view(),
    #      name='content_information'),
    re_path(r'^content/(?P<content_slug>[-\w]+)/information/$', views.ContentInformationView.as_view(),
         name='content_information'),

    # /products/content/4/review
    # path('content/<int:pk>/review/', views.ContentReviewView.as_view(),
    #      name='content_review'),

    # slug활용한 url 구성
    # /products/content/악어복불복-키트/review
    re_path(r'^content/(?P<content_slug>[-\w]+)/review/$', views.ContentReviewView.as_view(),
         name='content_review'),

    # /products/content/4/review/add
    re_path(r'^content/(?P<content_slug>[-\w]+)/review/add/$', views.content_review_add_view,
         name='content_review_add'),
    # /products/content/4/review/remove/3/
    re_path(r'^content/(?P<content_slug>[-\w]+)/review/remove/(?P<pk_appraisal>[0-9]+)$', views.content_review_remove_view,
         name='content_review_remove'),

    # # /products/product/4/review/edit
    # path('product/<int:pk>/review/edit/', views.product_review_edit_view,
    #      name='content_product_review_edit'),

    # /products/content/엔트리-어찌구/information/favorite/add
    re_path(r'^content/(?P<content_slug>[-\w]+)/information/favorite/add/$', views.content_information_favorite_add_view,
         name='content_information_favorite_add'),

    # /content/product/엔트리-어찌구/information/favorite/sub
    re_path(r'^content/(?P<content_slug>[-\w]+)/information/favorite/sub/$', views.content_information_favorite_sub_view,
         name='content_information_favorite_sub'),


    # /content/product/4/video/1/
    # path('content/<int:pk>/video/<int:pk_video>/', views.ContentVideoView.as_view(),
    #      name='content_video'),

    # slug활용한 url 구성
    # /content/product/엔트리-코딩/video/1/
    re_path(r'^content/(?P<content_slug>[-\w]+)/video/(?P<pk_video>[0-9]+)/$', views.ContentVideoView.as_view(),
         name='content_video'),

    # /content/product/4/video/1/reply/
    # path('content/<int:pk>/video/<int:pk_video>/reply', views.video_add_reply_view,
    #      name='content_video_reply'),

    # slug활용한 url 구성
    # /content/product/엔트리-코딩/video/1/reply/
    re_path(r'^content/(?P<content_slug>[-\w]+)/video/(?P<pk_video>[0-9]+)/reply/$', views.video_add_reply_view,
         name='content_video_reply'),

    # /content/product/4/video/1/reply/1/remove
    re_path(r'^content/(?P<content_slug>[-\w]+)/video/(?P<pk_video>[0-9]+)/reply/(?P<pk_reply>[0-9]+)/remove/$', views.video_remove_reply_view,
         name='content_video_reply_remove'),

    # /content/product/4/video/1/reply/1/edit
    re_path(r'^content/(?P<content_slug>[-\w]+)/video/(?P<pk_video>[0-9]+)/reply/(?P<pk_reply>[0-9]+)/edit$', views.video_edit_reply_view,
         name='content_video_reply_edit'),

    # /content/product/4/video/1/reply/1/reply
    re_path(r'^content/(?P<content_slug>[-\w]+)/video/(?P<pk_video>[0-9]+)/reply/(?P<pk_reply>[0-9]+)/reply$', views.video_reply_to_reply_view,
         name='content_video_reply_to_reply')

]
