from turtle import home
from django.urls import path, include

from .views import CityListView, CityRDView


urlpatterns = [
    path('api/', CityListView.as_view(),name='city-list'),
    path('api/<slug:slug>/',CityRDView.as_view(), name='city-detail')

]