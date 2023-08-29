from rest_framework import serializers
from .models import Profile, Friend, Chat, Message


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['self_profile']
        depth = 2


class ProfileSerializer(serializers.ModelSerializer):
    # the serializer will return a 'friend=profiles' object with multiple 'self-profiles' inside.
    friend_profiles = FriendSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 2


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        depth = 2


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        depth = 2

