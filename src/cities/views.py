from django.shortcuts import render, get_object_or_404

from cities.models import City

__all__ = (
    'home',
)

def home(request, pk=None):
    if pk:
        city = City.objects.filter(id=pk).first()
        # city = City.objects.get(pk=id) - возвращает DoesNotExist
        # city = get_object_or_404(City, pk=id) #- возвращает 404
        context = {"object": city}
        return render(request, 'cities/detail.html', context=context)
    qs = City.objects.all() #Получаем QuerySet из модели.
    context = {"objects": qs} # Вставляем полученный кверисет в словарь.
    return render(request, 'cities/home.html', context=context)
