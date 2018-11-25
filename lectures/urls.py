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


app_name = 'lectures'
urlpatterns = [
    # /lectures/
    #path('', views.LectureModelView.as_view(), name='index'),
    path('', views.LectureListView.as_view(), name='index'),
    # /lectures/#_list/
    path('entry_list/', views.EntryListView.as_view(), name='entry_list'),
    path('maker_list/', views.MakerListView.as_view(), name='maker_list'),
    path('scratch_list/', views.ScratchListView.as_view(), name='scratch_list'),
    # /lectures/99
    path('<int:pk>/', views.LectureDetailView.as_view(), name='lecture_detail'),
]