from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Auto, Make
from .forms import MakeForm

# Create your views here.
class MainView(LoginRequiredMixin, View):
    template_name = 'autos/auto_list.html'

    def get(self, request):
        mc = Make.objects.count()
        al = Auto.objects.all()

        context = {
            "make_count": mc,
            "auto_list": al
            }
        return render(request, self.template_name, context )
    
class MakeView(LoginRequiredMixin, View):
    pass
class MakeCreateView(LoginRequiredMixin, View):
    pass
class MakeUpdateView(UpdateView):
    pass
class MakeDeleteView(DeleteView):
    pass
class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto    
    pass
class AutoUpdateView(UpdateView):
    pass
class AutolDeleteView(DeleteView):
    pass
