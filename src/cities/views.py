from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.models import City

__all__ = (
    'home',
    'CityDetailView',
)

def home(request, pk=None):
    # if pk:
    #     city = City.objects.filter(id=pk).first()
        # city = City.objects.get(id=pk) - возвращает DoesNotExist
        # city = get_object_or_404(City, id=pk) #- возвращает 404
        # context = {"object": city}
        # return render(request, 'cities/detail.html', context=context)
    qs = City.objects.all() #Получаем QuerySet из модели.
    context = {"objects": qs} # Вставляем полученный кверисет в словарь.
    return render(request, 'cities/home.html', context=context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
