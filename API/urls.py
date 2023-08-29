from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'profiles', views.ProfileView, 'profile')
router.register(r'friends', views.FriendView, 'friend')


urlpatterns = [
    path('', include(router.urls)),
    path('add_friend', views.createFriendship)
]
