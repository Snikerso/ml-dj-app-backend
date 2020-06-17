from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Image
from .serializers import ImageSerializer
from rest_framework import status


class  ImageViewSet(viewsets.ModelViewSet):
        queryset = Image.objects.all()
        serializer_class = ImageSerializer

        