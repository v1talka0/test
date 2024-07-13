# hello_world_app/views.py
from django.shortcuts import render
from .models import Name

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        if name == 'Віталій':
            result = f'{name}, чоткий пацан'
        else:
            result = f'{name}, бабіджон'
        return render(request, 'hello_world_app/index.html', {'result': result})
    return render(request, 'hello_world_app/index.html')
