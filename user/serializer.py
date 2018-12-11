from rest_framework.serializers import ModelSerializer, SlugRelatedField
from django.contrib.auth import get_user_model

from user.models import Profile

User = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username','nickname']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

