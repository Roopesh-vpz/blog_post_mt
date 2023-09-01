from django.shortcuts import render

from rest_framework import viewsets

from .serializers import *
from .models import *

class PostView(viewsets.ModelViewSet):
    queryset =PostMaster.objects.all()
    serializer_class=PostSerializer

# Create your views here.
