from django.urls import path
from proyecto import views

urlpatterns = [
    path('', views.vista_login),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('usuario', views.usuario, name='usuario'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario'),
]
