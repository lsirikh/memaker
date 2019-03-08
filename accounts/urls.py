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
from django.urls import path, re_path, reverse_lazy

from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.contrib.auth import views


from accounts import views as account_views
from accounts.forms import PasswordChangeForm

app_name = 'accounts'


urlpatterns = [
    # /accounts/
    # re_path(r'^', include('django.contrib.auth.urls')),
    path('', account_views.AccountsIndexView.as_view(), name="index"),
    #path('', account_views.index_view, name="index"),
    # re_path(r'^login/$', login, {'template_name' : 'accounts/login.html'})
    re_path(r'^login/$', account_views.login_view, name='login'),
    re_path(r'^logout/$', account_views.logout_view, name="logout"),
    re_path(r'^withdrawal/$', account_views.withdrawal_view, name="withdrawal"),
    re_path(r'^withdrawal/done$', account_views.withdrawal_done_view, name="withdrawal_done"),
    re_path(r'^register/$', account_views.register_view, name="register"),
    re_path(r'^account-activation-sent/$', account_views.account_activation_sent, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            account_views.activate, name='activate'),

    re_path(r'^profile/$', account_views.profile_view, name="profile"),
    re_path(r'^profile/edit/$', account_views.edit_profile_view, name="edit_profile"),

    # path('password_change/', account_views.change_password_view, name='password_change'),

    re_path(r'^order/$', account_views.order_status_view, name="order_status"),
    # re_path(r'^order/detail$', account_views.order_detail_view, name="order_detail"),
    # re_path(r'^order/edit$', account_views.order_edit_view, name="order_edit"),



    path('find-id/', account_views.find_id_view, name='find_id'),

    path('password-change/', PasswordChangeView.as_view(
        form_class = PasswordChangeForm,
        success_url=reverse_lazy('accounts:password_change_done'),
        template_name='accounts/password_change.html',
    ), name='password_change'),

    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html',
    ), name='password_change_done'),

    # reset password urls
    path('password-reset/',
         views.PasswordResetView.as_view(
             # success_url=reverse_lazy('accounts:password_reset_done'),
             #from_email ='help@openfingers.com',
             success_url=reverse_lazy('accounts:password_reset_done'),
             template_name='accounts/password_reset_form.html',
             email_template_name='accounts/password_reset_email.html',
             subject_template_name='accounts/password_reset_subject.txt'
         ), name='password_reset'),

    path('password-reset/done/', views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),

    path('password-reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),

    path('password-reset/confirm/done/', views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html',
    ), name='password_reset_complete')

]
