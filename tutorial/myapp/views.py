from django.shortcuts import render
from rest_framework import viewsets
from myapp.serializers import PersonSerializer
from myapp.models import Person
# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
