from rest_framework import serializers
from .models import Profile, Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['friend_profile']
        depth = 2


class ProfileSerializer(serializers.ModelSerializer):
    friend_profiles = FriendSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 2
