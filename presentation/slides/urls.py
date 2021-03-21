from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('presentations', views.PresentationView)
router.register('slides', views.SlidesView)

urlpatterns = [
    path('', include(router.urls))
]