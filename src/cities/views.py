from django.shortcuts import render

from cities.models import City

__all__ = (
    'home',
)

def home(request):
    qs = City.objects.all() #Получаем QuerySet из модели.
    context = {"objects": qs} # Вставляем полученный кверисет в словарь.
    return render(request, 'cities/home.html', context=context)
