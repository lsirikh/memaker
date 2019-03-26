from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('<int:pk>/content/<int:quantity>/create/',
         views.order_one_create, name='order_one_create'),
    path('create/mobile', views.order_create_mobile, name='order_create_mobile'),
    path('create/initial-processing', views.order_initial_processing, name='order_initial_processing'),
    path('create/confirm', views.order_payment_confirm, name='order_payment_confirm'),

    path('payment/confirm/', views.order_confirm, name='order_confirm'),
    path('payment/cancel/', views.order_cancel, name='order_cancel'),
]