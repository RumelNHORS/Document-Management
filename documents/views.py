from rest_framework import generics, permissions
from django.contrib.auth.models import User
from documents import models
from documents import serializers


# View for user signup
class UserSignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

# View for user login
class UserLogin(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

# View for listing and creating documents
class DocumentList(generics.ListCreateAPIView):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

# View for retrieving, updating, and deleting documents
class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

# View for updating document shares
class DocumentShareUpdate(generics.UpdateAPIView):
    queryset = models.DocumentShare.objects.all()
    serializer_class = serializers.DocumentShareSerializer
    permission_classes = [permissions.IsAuthenticated]
