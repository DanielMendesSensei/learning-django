"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.http import HttpResponse
#from home import views as home_views
#from blog import views as blog_views

#HTTP request cliente <-> HTTP response servidor
#MVT Model View Template (MVC) Variação de Padrão de projeto Model View Controler

#Testando http requeste e response com funções, seguindo a views
# do padrão de projeto MVT, recebe o nome function based views, pois foi
# feito com funções e não classes
"""def my_view(request):#1
    print("Cliente clicou")
    return HttpResponse("UMA MENSAGEM")

def home(request):#2
    print("Cliente clicou na HOME")
    return HttpResponse("HOME")
"""

#https://dominio.com/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),# include está importando da pasta app home o arquivo urls.py
    path('blog/', include('blog.urls'))# include está importando da pasta app blog o arquivo urls.py
    # Fazendo dessa forma, com urls dentro de cada app, fazemos o aninhamento de URLS
    # O Que torna mais fácil a inserção de urls internas do app
    # Evitando por coisas do tipo
    # path('blog/exemplo', blog_views.exemplo)

    #____________________________________
    # path('', home_views.index),
    # path('blog/', blog_views.index)
    # path('blog', my_view),#1
    # path('',home) # endereço raiz do sistema #2
]
