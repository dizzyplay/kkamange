from django.contrib.auth import get_user_model, logout
from .serializers import UserSerializer, ProfileSerializer

User = get_user_model()


def jwt_response_payload_handler(token, user=None, request=None):
    profile = user.profile_set.get(user=user)
    serializer = ProfileSerializer(profile)
    return {
        'token': token,
        'profile':serializer.data
    }
