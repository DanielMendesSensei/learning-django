from django.urls import path
from . import views #Importação relativa da pasta subpasta

app_name = 'blog'

urlpatterns = [
    path('<int:post_id>/', views.posts, name='post'), #sempre deixa uma barra no final
    #path('posts/<int:post_id>/', views.posts, name='post'), #sempre deixa uma barra no final
    path('', views.index, name='index'),
    #path('exemplo/', views.exemplo)
]
