from django.shortcuts import render
from rest_framework import generics
from .models import MarketReport
from .serializers import MyModelSerializer
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')

class MyModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = MarketReport.objects.all()
    serializer_class = MyModelSerializer
