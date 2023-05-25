from django.shortcuts import render
from blog.templates.blog import data
from django.http import HttpResponse, Http404
from typing import Any


# Quando você estiver refatorando,
# não faz com control x, nunca tira o que está rodando

def index(request):
    print('Blog')
    context = {
        'text': 'Olá, esse é o blog',
        'title': 'Blog',
        'posts': data.data_posts,
    }
    return render(
        request,
        'blog/index.html',
        context,
    )

def posts(request: HttpResponse, post_id: int):
    #tipagem de variável para tipo dicionario, recebendo sua chave como string, e valor como qualquer um
    #vem da biblioteca typing Any. Ou então sendo None
    found_post: dict[str, Any] or None = None

    #laço da lista, em arquivos do data.py
    for post in data.data_posts:
        if post['id'] == post_id:
            found_post = post
            break

    #print(f'Você está no post: {post_id}')

    #condicional se caso o valor ainda for None, ou seja, não está na lista
    if found_post is None:
        raise Http404("POST NÃO EXISTE")

    context = {
        #'text': 'Olá, esse é o blog',
        'posts': [found_post],
        'title': found_post['title'],
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