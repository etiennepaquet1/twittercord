from django.db import models
import string
import random
# Create your models here.


def generate_code():
    length = 16
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Profile.objects.filter(code=code).count() == 0:
            break
    return code


class Profile(models.Model):
    code = models.CharField(primary_key=True, max_length=16, default="", unique=True)  # how to make it required?
    # user: User
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=4096, default='')
    stranger_can_see = models.BooleanField(null=False, default=False) # add ProfileSettings model?
    stranger_can_mssg = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Friend(models.Model):
    friend_profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="friend_profiles")
    self_profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="self_profiles")


class Chat(models.Model):
    chat_id: models.IntegerField(primary_key=True, unique=True)
    type: models.CharField(max_length=64, default="DM")
    chat_name: models.CharField(max_length=512, default="", unique=False)
    members = [models.ForeignKey('Profile', on_delete=models.DO_NOTHING, related_name='ChatMembers')]


class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.DO_NOTHING, related_name='messages')
    senderId = models.CharField(max_length=16, default='', unique=False)  # Profile ID of who sent the message
    content = models.CharField(max_length=1048576, default='', unique=False)
    timedate = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(null=False, default=False)

