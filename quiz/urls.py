from django.urls import path
from . import views

urlpatterns = [
    path('', views.guess, name='guess'),
    path('result/', views.result, name='result')
]
