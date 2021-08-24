from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('registro/', views.registroUsuario, name="registro"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
    
]
