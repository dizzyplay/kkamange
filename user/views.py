from django.contrib.auth import get_user_model, logout
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile

User = get_user_model()


def jwt_response_payload_handler(token, user,request=None):
    profile = Profile.objects.get(user=user)
    serializer = ProfileSerializer(profile)
    return {
        'token': token,
        'profile':serializer.data,
        'username':user.username,
    }
