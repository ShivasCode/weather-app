from django.shortcuts import render
from rest_framework import generics

from .models import City 
from .serializers import CitySerializer



class CityListView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'pk'


