from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .models import Presentations, Slides
from .serializers import PresentationSerializer, SlidesSerializer

class IndexView(View):

    def get(self, request):
        return render(request, 'slides/index.html')

# API views ----------------------------------

class PresentationView(viewsets.ModelViewSet):
    queryset = Presentations.objects.all()
    serializer_class = PresentationSerializer


class SlidesView(viewsets.ModelViewSet):
    queryset = Slides.objects.all()
    serializer_class = SlidesSerializer
