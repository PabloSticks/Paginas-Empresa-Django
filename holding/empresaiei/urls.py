from django.urls import path
from .views import inicio, nuestra, contacto

urlpatterns = [
    path('', inicio, name='inicio'),  
    path('nuestra/', nuestra, name='nuestra'),
    path('contacto/', contacto, name='contacto'),
]