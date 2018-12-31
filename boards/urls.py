from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from boards import views

app_name = 'boards'
urlpatterns = [
    path('', views.BoardsIndexView.as_view(), name="index"),
    path('<int:pk>/', views.TopicListView.as_view(), name="board_topic"),
    #path('<int:pk>/', views.board_content_list_view, name="board_topic"),
    path('<int:pk>/content/<int:topic_pk>/', views.BoardsContentView.as_view(), name="board_content"),
    #path('<int:pk>/content/<int:topic_pk>/', views.see_content_view, name="board_content"),
    path('<int:pk>/content/<int:topic_pk>/edit/', views.edit_content_view, name="edit_content"),
    path('<int:pk>/content/<int:topic_pk>/remove/', views.remove_content_view, name="remove_content"),
    path('<int:pk>/content/<int:topic_pk>/reply/', views.add_reply_view, name="add_reply"),
    #path('<int:pk>/content/<int:topic_pk>/reply/', views.AddReplyView.as_view(), name="add_reply"),
    path('<int:pk>/content/<int:topic_pk>/reply/<int:post_pk>/edit/', views.edit_reply_view, name="edit_reply"),
    path('<int:pk>/content/<int:topic_pk>/reply/<int:post_pk>/remove/', views.remove_reply_view, name="remove_reply"),
    path('<int:pk>/content/<int:topic_pk>/reply/<int:post_pk>/reply/', views.add_reply_to_reply_view, name="reply_to_reply"),
    #path('<int:pk>/content/<int:topic_pk>/reply/<int:post_pk>/<slug:slug>/', views.add_reply_to_reply_view, name="reply_to_reply"),
    path('<int:pk>/add/', views.add_content_view, name="add_content")
]
