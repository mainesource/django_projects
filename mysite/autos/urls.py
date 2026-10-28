from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = "autos"

urlpatterns = [
        path("", views.MainView.as_view(), name='all' ),
        path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
        path('main/<int:pk>/update/', views.AutoUpdateView.as_view(), name='auto_update'),
        path('main/<int:pk>/delete/', views.AutolDeleteView.as_view(), name='auto_delete'),
        path('lookup/', views.MakeView.as_view(), name='make_list'),
        path('lookup/create/', views.MakeCreateView.as_view(), name='make_create'),
        path('lookup/<int:pk>/update/', views.MakeUpdateView.as_view(), name='make_update'),
        path('lookup/<int:pk>/delete/', views.MakeDeleteView.as_view(), name='make_delete'),
        ]
