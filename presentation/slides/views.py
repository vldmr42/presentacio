from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .models import Presentations, Slides
from .serializers import PresentationSerializer, SlidesSerializer
from .forms import UserRegisterForm, AuthenticationForm


class IndexView(View):

    def get(self, request):
        context = {}
        user_reg_form = UserRegisterForm()
        context['user_reg_form'] = user_reg_form

        user_login_form = AuthenticationForm()
        context['user_login_form'] = user_login_form

        return render(request, 'slides/index.html', context=context)

    def post(self, request):
        if 'login' in request.POST:
            # logging user in
            form = AuthenticationForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'User - {user}, just logged in.')
                    return redirect('index')
                else:
                    messages.error(request, 'Invalid login or password.')
                    return redirect('index')
            else:
                messages.error(request, 'Form is not pass the validation.')
                return redirect('index')

        elif 'register' in request.POST:
            # registering user
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are able to login now.{username}!')
                return redirect('index')
        else:
            messages.info(request, 'No register or login keys in POST dic.')
            return redirect('index')


# API views ----------------------------------

class PresentationView(viewsets.ModelViewSet):
    queryset = Presentations.objects.all()
    serializer_class = PresentationSerializer


class SlidesView(viewsets.ModelViewSet):
    queryset = Slides.objects.all()
    serializer_class = SlidesSerializer
