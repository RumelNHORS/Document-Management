from rest_framework import serializers
from django.contrib.auth.models import User
from documents import models

# Serializer for user signup and login
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

# Serializer for documents
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Document
        fields = '__all__'

# Serializer for document shares
class DocumentShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DocumentShare
        fields = '__all__'
