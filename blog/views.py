from django.shortcuts import render
from blog.templates.blog import data
#from django.http import HttpResponse


# Quando você estiver refatorando,
# não faz com control x, nunca tira o que está rodando

def index(request):
    print('Blog')
    context = {
        'text': 'Olá, esse é o blog',
        'title': 'Blog',
        'posts': data.posts,
    }
    return render(
        request,
        'blog/index.html',
        context,
    )

def posts(request, id):
    print(f'Você está no post: {id}')
    context = {
        #'text': 'Olá, esse é o blog',
        #'title': 'Blog',
        'posts': data.posts,
    }
    return render(
        request,
        'blog/index.html',
        context,
    )

'''
def index(request):
    print('Blog')
    return HttpResponse("BLOG")

def exemplo(request):
    print('Exemplo-Blog')
    return HttpResponse("Exemplo Blog")
'''