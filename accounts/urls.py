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

from django.contrib.auth import views as auth_views

from accounts import views as account_views

app_name = 'accounts'
urlpatterns = [
    # /accounts/
    # re_path(r'^', include('django.contrib.auth.urls')),
    re_path(r'^$', account_views.AccountsIndexView.as_view(
    ), name="index"),
    # re_path(r'^login/$', login, {'template_name' : 'accounts/login.html'})
    re_path(r'^login/$', account_views.login_view, name='login'),
    re_path(r'^logout/$', account_views.logout_view, name="logout"),
    re_path(r'^register/$', account_views.register_view, name="register"),
    re_path(r'^profile/$', account_views.profile_view, name="profile"),
    re_path(r'^profile/edit/$', account_views.edit_profile_view, name="edit_profile"),

    # path('password_change/', account_views.change_password_view, name='password_change'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        # form_class = PasswordChangeForm,
        success_url=reverse_lazy('accounts:password_change_done'),
        template_name='accounts/password_change.html',
    ), name='password_change'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/index.html',
    ), name='password_change_done'),

    # reset password urls
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             #success_url=reverse_lazy('accounts:password_reset_done'),
             #template_name='accounts/password_reset_form.html',
             #email_template_name='accounts/password_reset_email.html',
         ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(

    ), name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
         ), name='password_reset_complete')

]
