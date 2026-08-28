from django.shortcuts import render


def home(request):
    context = {
        'titulo': 'Sesión 1',
        'lema': 'Construye aplicaciones empresariales modernas con Django',
    }
    return render(request, 'landing/home.html', context)
