from rest_framework import serializers
from django.contrib.auth.models import User
from test_auth_service_API.models import Perm
from test_auth_service_API.models import Role
from django.contrib.auth.hashers import make_password
from django.forms.models import model_to_dict


class PermSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #roles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Perm
        fields = ['id', 'title', 'description', 'owner']

class RoleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    perms = PermSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'owner', 'perms']

class UserSerializer(serializers.ModelSerializer):
    #perms = PermSerializer(many=True, read_only=True)
    roles = RoleSerializer(many=True, read_only=True)
    # name = serializers.SerializerMethodField()

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'username', 'roles']    

    # def get_name(self, profile):
    #       return profile.perms

    def create(self, validated_data):
       # create user 
       user = User.objects.create(
           #first_name = validated_data['first_name'],
           #last_name = validated_data['last_name'],
           email = validated_data['email'],
           username = validated_data['username'],
           password = make_password(validated_data['password'])
       )
       return user