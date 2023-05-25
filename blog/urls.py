from django.urls import path
from . import views #Importação relativa da pasta subpasta

app_name = 'blog'

urlpatterns = [
    path('posts/<int:id>/', views.posts, name='post'), #sempre deixa uma barra no final
    path('', views.index, name='index'),
    #path('exemplo/', views.exemplo)
]
