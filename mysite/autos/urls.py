from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = "autos"

urlpatterns = [
        path("", TemplateView.as_view(template_name="solo1.html"), name='solo1'), 
        ]
