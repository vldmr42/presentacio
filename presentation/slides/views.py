from django.shortcuts import render
from django.views import View
from django.contrib import messages
from rest_framework import viewsets
from .models import Presentations, Slides
from .serializers import PresentationSerializer, SlidesSerializer
from .forms import UserRegisterForm, AuthenticationForm


class IndexView(View):
    context = {}
    user_reg_form = UserRegisterForm()
    context['user_reg_form'] = user_reg_form

    user_login_form = AuthenticationForm()
    context['user_login_form'] = user_login_form

    def get(self, request):
        return render(request, 'slides/index.html', context=self.context)


# API views ----------------------------------

class PresentationView(viewsets.ModelViewSet):
    queryset = Presentations.objects.all()
    serializer_class = PresentationSerializer


class SlidesView(viewsets.ModelViewSet):
    queryset = Slides.objects.all()
    serializer_class = SlidesSerializer
