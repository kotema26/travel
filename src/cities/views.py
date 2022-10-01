from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from cities.forms import HtmlForms, CityForm
from cities.models import City

__all__ = (
    'home',
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
)

def home(request, pk=None):
    # if pk:
    #     city = City.objects.filter(id=pk).first()
        # city = City.objects.get(id=pk) - возвращает DoesNotExist
        # city = get_object_or_404(City, id=pk) #- возвращает 404
        # context = {"object": city}
        # return render(request, 'cities/detail.html', context=context)
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = CityForm()  #Созд. экземпляр класса и передаем в словарь.
    qs = City.objects.all()  #Получаем QuerySet из модели.
    context = {"objects": qs, "form": form}  # Вставляем полученный кверисет в словарь.
    return render(request, 'cities/home.html', context=context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')

class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')

