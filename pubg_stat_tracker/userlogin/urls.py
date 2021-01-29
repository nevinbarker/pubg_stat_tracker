from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='userlogin-register'),
    path('login', views.login, name='userlogin-login')
]