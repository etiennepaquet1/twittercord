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
    self_profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="friend_profiles")
    friend_profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="self_profiles")
    # DMs: Chat



