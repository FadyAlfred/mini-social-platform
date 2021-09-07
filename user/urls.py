from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user.views import UserViewSet, FriendViewSet, FriendRequestViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'friends', FriendViewSet, basename='friends')
router.register(r'friends/requests', FriendRequestViewSet, basename='friends-requests')

urlpatterns = [
    path('', include(router.urls)),
]
