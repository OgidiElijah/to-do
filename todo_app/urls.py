from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'list'),
    path('modify/<str:pry_key>', views.modifyTask, name="modify"),
    path('delete/<str:pry_key>', views.deleteTask, name="delete"),
]