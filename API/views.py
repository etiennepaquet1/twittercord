from rest_framework import viewsets
from .serializers import ProfileSerializer, FriendSerializer
from .models import Profile, Friend


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class FriendView(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


def createFriendship(request, self_profile, friend_profile):
    friend = Friend(self_profile=self_profile, friend_profile=friend_profile)
    friend.save()


