from django.shortcuts import render
from rest_framework import permissions, viewsets, status
# from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action, api_view, permission_classes
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.
# Class-based views
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAdminUser]
    
#     @action(detail=True, methods=['post'])
#     def set_password(self, request, pk=None):
#         user = self.get_object()
        

# Function-based views
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        queryset = get_user_model().objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    if request.method == 'GET':
        queryset = get_object_or_404(get_user_model(), pk=pk)
        # queryset = get_user_model().objects.filter(pk=pk)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        queryset = get_user_model().objects.filter(pk=pk)
        if request.user == queryset:
            serializer = UserSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    elif request.method == 'DELETE':
        queryset = get_user_model().objects.filter(pk=pk)
        if request.user == queryset:
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)