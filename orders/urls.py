from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('<int:pk>/content/<int:num>/create/',
         views.order_one_create, name='order_one_create'),
    path('confirm/', views.order_confirm, name='order_confirm'),
    path('cancel/', views.order_cancel, name='order_cancel'),
]