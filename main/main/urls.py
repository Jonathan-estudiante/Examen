from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('', include(('tickets.urls', 'tickets'), namespace='tickets')),

]
