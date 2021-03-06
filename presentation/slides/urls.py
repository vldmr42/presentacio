from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('presentations', views.PresentationView)
router.register('slides', views.SlidesView)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/', include(router.urls), name='api_root')
]