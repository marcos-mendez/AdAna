from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='images'),
    path('static/images/', views.home, name='images'),
]