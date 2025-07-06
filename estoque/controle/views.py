from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

from .models import Produto

# Create your views here.
def home(request):
    return render(request, "controle/home.html")

def produtos_views(request):

    if request.method == 'POST':
        cod_produto = request.POST.get('cod_produto')
        nome = request.POST.get('nome')
        categoria = request.POST.get('controle_atual')
        controle_atual = request.POST.get('controle_atual')
        controle_minimo = request.POST.get('controle_minimo')


        if cod_produto and nome and categoria and controle_atual and controle_minimo:
            Produto.objects.create(
                cod_produto=cod_produto,
                nome=nome,
                categoria=categoria,
                controle_atual=controle_atual,
                controle_minimo=controle_minimo
            )
            return redirect('produtos')
        
        produtos = Produto.objects.all().order_by('cod_produto')
        return render(request, 'controle/home.html', {'produtos': produtos})