from django.urls import path
from .views import *

app_name = 'cats'
urlpatterns = [
    path('', CatListView.as_view(), name='all_cats'),
    path('cat/create/', CatCreateView.as_view(), name='create_cat'),
    path('cat/<int:pk>/detail/', CatDetailView.as_view(), name='detail_cat'),
    path('cat/<int:pk>/update/', CatUpdateView.as_view(), name='update_cat'),
    path('cat/<int:pk>/delete/', CatDeleteView.as_view(), name='delete_cat'),
    path('breeds/', BreedListView.as_view(), name='all_breeds'),
    path('breed/create/', BreedCreateView.as_view(), name='create_breed'),
    path('breed/<int:pk>/update/', BreedUpdateView.as_view(), name='update_breed'),
    path('breed/<int:pk>/delete/', BreedDeleteView.as_view(), name='delete_breed'),
]
