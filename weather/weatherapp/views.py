from django.shortcuts import render
from rest_framework import generics
from rest_framework import status

from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import City 
from .serializers import CitySerializer
from rest_framework.views import APIView



class CityListView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# class CityListView(APIView):
#     def list(self, request):
#         query = City.objects.all()
#         serializer = CitySerializer(City, many=True)
#         return Response(serializer.data)


class CityRDView(generics.RetrieveDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'slug'


# class CityRDView(APIView):
#     def get_object(self,pk):
#         query = get_object_or_404(City, pk=pk)
#         return query
#     def get(self,request,pk):
#         job = self.get_object(pk)
#         serializer = CitySerializer(job)
#         return Response(serializer.data)

#     def delete(self,request,pk):
#         job = self.get_object(pk)
#         job.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
