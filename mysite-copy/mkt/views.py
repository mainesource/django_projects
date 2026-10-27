from django.shortcuts import render
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Ad
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AdListView(LoginRequiredMixin, OwnerListView):
    model = Ad
    fields = '__all__'

class AdDetailView(OwnerDetailView):
    model = Ad
    fields = ['title', 'price', 'text',]

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text',]

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text',]

class AdDeleteView(OwnerDeleteView):
    model = Ad
    fields = '__all__'
