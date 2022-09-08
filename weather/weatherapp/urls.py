from turtle import home
from django.urls import path, include

from .views import CityListView, CityRUDView


urlpatterns = [
    path('api/', CityListView.as_view()),
    path('api/<slug:slug>/',CityRUDView.as_view())

]