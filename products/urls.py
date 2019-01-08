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
from django.urls import path

app_name = 'products'
urlpatterns = [
    # path('', views.ProductModelView.as_view(), name='index'),
    # /products/product-list
    path('product-list/', views.ProductListView.as_view(),
         name='product_list'),
    # /products/lecture-list/
    path('lecture-list/', views.LectureListView.as_view(),
         name='lecture_list'),
    # /products/category-list/4/
    path('category-list/<int:pk>/', views.ContentCategoryListView.as_view(),
         name='content_category_list'),

    # /products/content/4/information
    path('content/<int:pk>/information/', views.ContentInformationView.as_view(),
         name='content_information'),
    # /products/content/4/review
    path('content/<int:pk>/review/', views.ContentReviewView.as_view(),
         name='content_review'),

    # /products/content/4/review/add
    path('content/<int:pk>/review/add/', views.content_review_add_view,
         name='content_review_add'),
    # /products/content/4/review/remove/3/
    path('content/<int:pk>/review/remove/<int:pk_appraisal>', views.content_review_remove_view,
         name='content_review_remove'),

    # # /products/product/4/review/edit
    # path('product/<int:pk>/review/edit/', views.product_review_edit_view,
    #      name='content_product_review_edit'),

    # /products/content/4/information/favorite/add
    path('content/<int:pk>/information/favorite/add', views.content_information_favorite_add_view,
         name='content_information_favorite_add'),

    # /content/product/4/information/favorite/sub
    path('content/<int:pk>/information/favorite/sub/', views.content_information_favorite_sub_view,
         name='content_information_favorite_sub'),


    # /content/product/4/video/1/
    path('content/<int:pk>/video/<int:pk_video>/', views.ContentVideoView.as_view(),
         name='content_video'),

    # /content/product/4/video/1/reply/
    path('content/<int:pk>/video/<int:pk_video>/reply', views.video_add_reply_view,
         name='content_video_reply'),

    # /content/product/4/video/1/reply/1/remove
    path('content/<int:pk>/video/<int:pk_video>/reply/<int:pk_reply>/remove', views.video_remove_reply_view,
         name='content_video_reply_remove'),

    # /content/product/4/video/1/reply/1/edit
    path('content/<int:pk>/video/<int:pk_video>/reply/<int:pk_reply>/edit', views.video_edit_reply_view,
         name='content_video_reply_edit'),

    # /content/product/4/video/1/reply/1/reply
    path('content/<int:pk>/video/<int:pk_video>/reply/<int:pk_reply>/reply', views.video_reply_to_reply_view,
         name='content_video_reply_to_reply'),

    # path('unpluged_list/', views.UnplugedListView.as_view(), name='unpluged_list'),
    # path('kit_list/', views.KitListView.as_view(), name='kit_list'),
    # path('book_list/', views.BookListView.as_view(), name='book_list'),
    # path('board_list/', views.BoardListView.as_view(), name='board_list'),
    # # /products/11/99
    # path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    # path('add/<int:pk>/', views.favorite_add_view, name='favorite_add'),
    # path('sub/<int:pk>/', views.favorite_sub_view, name='favorite_sub'),
]
