from django.shortcuts import render
from goods.models import Categories

def index(request):
    context = {
        'title': 'Главная страница',
        'categories':  Categories.objects.all(),
    }


    return render(request, 'main/index.html', context=context)
