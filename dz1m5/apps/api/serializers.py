from dataclasses import fields
from rest_framework import serializers
from apps.api.models import Task

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields= '__all__'
        