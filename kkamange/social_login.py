from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class NaverLogin(SocialLoginView):
    adapter_class = NaverOAuth2Adapter

