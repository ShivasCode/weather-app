from turtle import home
from django.urls import path, include

from .views import CityListView


urlpatterns = [
    path('api/', CityListView.as_view())
]