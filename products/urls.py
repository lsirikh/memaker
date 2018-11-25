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
from . import views
from django.urls import path


app_name = 'products'
urlpatterns = [
    # /products/
    #path('', views.ProductModelView.as_view(), name='index'),
    path('', views.ProductListView.as_view(), name='index'),
    # /products/#_list/
    path('unpluged_list/', views.UnplugedListView.as_view(), name='unpluged_list'),
    path('kit_list/', views.KitListView.as_view(), name='kit_list'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('board_list/', views.BoardListView.as_view(), name='board_list'),
    # /products/11/99
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]