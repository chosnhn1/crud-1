from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all().order_by('-pk')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    