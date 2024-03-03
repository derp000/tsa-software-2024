from django.shortcuts import render
from myapi.models import Person

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    person = Person.objects.all()
    return Response({'message': str(person)})