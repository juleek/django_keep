from django.urls import re_path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    re_path('create/$', views.create_account, name='create_account'),
    re_path('login_user/$', views.login_user, name='login'),
    re_path('logout/$', auth_views.LogoutView.as_view(), name='logout'),

    re_path('change_password/$', views.change_password, name='change_password'),
    re_path('my_account/$', views.UserUpdateView.as_view(), name='my_account')
]
