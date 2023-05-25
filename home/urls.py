from django.urls import path
from . import views #Importação relativa da pasta subpasta

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index')
]
