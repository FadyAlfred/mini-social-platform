from rest_framework import serializers
from django.contrib.auth.models import User
from rest_auth.registration.serializers import RegisterSerializer
from friendship.models import FriendshipRequest


class RegistrationSerializer(RegisterSerializer):
  first_name = serializers.CharField(required=False)
  last_name = serializers.CharField(required=False)

  def custom_signup(self, request, user):
    user.first_name = self.validated_data.get('first_name', '')
    user.last_name = self.validated_data.get('last_name', '')
    user.save(update_fields=['first_name', 'last_name'])


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username']


class UserDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email']


class CreateFriendRequestSerializer(serializers.Serializer):
  user_id = serializers.IntegerField()


class FriendRequestSerializer(serializers.ModelSerializer):
  class Meta:
    model = FriendshipRequest
    fields = ['id', 'from_user', 'to_user', 'message', 'created', 'rejected', 'viewed']