from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homeview, name='homepage'),
    path('cat/', views.Catview, name='catview'),
    path('dog/', views.Dogview, name='dogview'),
]
