from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.model import Auto, Make
from autos.forms import MakeForm

# Create your views here.
class MainView(LoginRequiredMixin, View):
    pass
class MakeListView(ListView):
    pass
class MakeDetailView(DetailView):
    pass
class MakeUpdateView(UpdateView):
    pass
class MakeDeleteView(DeleteView):
    pass
class ModelListView(ListView):
    pass
class ModelDetailView(DetailView):
    pass
class ModelUpdateView(UpdateView):
    pass
class ModelDeleteView(DeleteView):
    pass
