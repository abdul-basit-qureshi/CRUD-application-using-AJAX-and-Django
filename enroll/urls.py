from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('save/', views.saveData, name='save'),
    path('delete/', views.deleteData, name='delete'),
    path('edit/', views.editData, name='edit'),
]