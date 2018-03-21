from django.shortcuts import render

# import Response from the rest_framework response module. This will handle the response from the API requests
from rest_framework.response import Response
# import APIView that will act as a base class for the API view function
from rest_framework.views import APIView
#import UserInformation class from the models
from .models import UserInformation
#import UserInformationSerializer class from the serializer module
from .serializer import UserInformationSerializer
# Create your views here.
