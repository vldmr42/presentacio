from django.shortcuts import render
from rest_framework import viewsets
from .models import Presentations, Slides
from .serializers import PresentationSerializer, SlidesSerializer


class PresentationView(viewsets.ModelViewSet):
    queryset = Presentations.objects.all()
    serializer_class = PresentationSerializer


class SlidesView(viewsets.ModelViewSet):
    queryset = Slides.objects.all()
    serializer_class = SlidesSerializer
