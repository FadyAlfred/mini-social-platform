from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, decorators, permissions
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from friendship.models import Friend, FriendshipRequest

from .serializers import UserSerializer, UserDetailSerializer, CreateFriendRequestSerializer, \
    FriendRequestSerializer


class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        """
        This view for listing all users
        """
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        This view for retrieving user by id
        """
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class FriendViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        """
        This view for listing all friends
        """
        friends = Friend.objects.friends(request.user)
        serializer = UserSerializer(friends, many=True)
        return Response(serializer.data)


class FriendRequestViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        """
        This view for listing all friends requests
        """
        friend_requests = Friend.objects.unrejected_requests(user=request.user)
        serializer = FriendRequestSerializer(friend_requests, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        This view for sending a friend request
        """
        serializer = CreateFriendRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        friend_id = serializer.data.get('user_id')
        friend_obj = Friend.objects.add_friend(
            request.user,
            get_object_or_404(User, pk=friend_id),
            message=request.data.get('message', '')
        )
        friend_request_serializer = FriendRequestSerializer(friend_obj)
        return Response(friend_request_serializer.data, status.HTTP_201_CREATED)

    @decorators.action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        """
        This view for accepting a friends requests
        """
        friendship_request = get_object_or_404(FriendshipRequest, pk=pk, to_user=request.user)
        friendship_request.accept()
        serializer = FriendRequestSerializer(friendship_request)
        return Response(serializer.data, status.HTTP_201_CREATED)

    @decorators.action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        """
        This view for rejecting a friends requests
        """
        friendship_request = get_object_or_404(FriendshipRequest, pk=pk, to_user=request.user)
        friendship_request.reject()
        serializer = FriendRequestSerializer(friendship_request)
        return Response(serializer.data, status.HTTP_201_CREATED)
