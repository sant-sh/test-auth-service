from rest_framework import generics
from test_auth_service_API import serializers
from django.contrib.auth.models import User
from test_auth_service_API.models import Perm
from rest_framework import permissions
from test_auth_service_API.permissions import IsOwnerOrReadOnly
from test_auth_service_API.models import Role
from rest_framework import status
from rest_framework.response import Response

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def post(self, request, format=None):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class PermList(generics.ListCreateAPIView):
    queryset = Perm.objects.all()
    serializer_class = serializers.PermSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PermDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perm.objects.all()
    serializer_class = serializers.PermSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = serializers.RoleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = serializers.RoleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]