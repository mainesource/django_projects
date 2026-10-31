from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Breed, Cat
from django.utils import timezone
from django.urls import reverse_lazy



# Create your views here.

class CatListView(LoginRequiredMixin, ListView):
    model = Cat
    template = 'cats/all_cats.html'
    def get(self, request):
        ac = Cat.objects.all()
        bc = Breed.objects.count()
        context = {
                'breed_count':bc,
                'all_cats': ac,
                }
        return render(request, self.template, context)

class CatDetailView(LoginRequiredMixin, DetailView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')

class CatCreateView(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    #template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all_cats')    

class CatUpdateView(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')

class CatDeleteView(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')
    

class BreedListView(LoginRequiredMixin, ListView):
    model = Breed
    fields = '__all__'

class BreedCreateView(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')

class BreedUpdateView(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')

class BreedDeleteView(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')


    
   


    
        






