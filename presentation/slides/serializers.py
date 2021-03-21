from rest_framework import serializers
from .models import Presentations, Slides

class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentations
        fields = ('id', 'name', 'created', 'slides')

class SlidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slides
        fields = (
            'id',
            'presentation_id',
            'order_number',
            'text',
            'align',
            'color',
            'size'
        )