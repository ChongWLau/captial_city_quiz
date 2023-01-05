from django.urls import path
from . import views

urlpatterns = [
    path('', views.guess, name='guess'),
    path('result/<str:country>/<str:guess>/', views.result, name='result')
]
