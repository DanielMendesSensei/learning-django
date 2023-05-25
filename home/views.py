from django.shortcuts import render
# Quando você estiver refatorando,
# não faz com control x, nunca tira o que está rodando

# Create your views here.
def index(request):
    print('HOME')
    context = {
        'text': 'Olá, essa é a home',
        'title': 'Home',
    }
    return render(
        request,
        'home/index.html',
        context) #O argumento contexto serve para fazermos atualizações mediante a estrutura de dicionários
