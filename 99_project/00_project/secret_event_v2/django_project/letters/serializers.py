from rest_framework import serializers
from .models import Letter

class LettersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'