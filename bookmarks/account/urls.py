from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    #NAS URLS INICIAIS, ADICIONAMOS O PATH PARA A VIEW DE LOGIN
    path('login/', views.user_login, name='login'),         
    #path('login/', views.user_login, name='login'),
]

