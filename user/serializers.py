from rest_framework.serializers import ModelSerializer, SlugRelatedField
from django.contrib.auth import get_user_model

from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from user.models import Profile

User = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nickname','gender']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


# for rest-auth
class UserProfileSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username','profile']


class SignUpSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, write_only=True)
    gender = serializers.ChoiceField(choices=Profile.GENDER_CHOICES, default=Profile.GENDER_CHOICES[2][0])

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'gender': self.validated_data.get('gender', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        user = super().save(request)
        user_profile = Profile(user=user, nickname=self.cleaned_data['nickname'], gender=self.cleaned_data['gender'])
        user_profile.save()
        return user
