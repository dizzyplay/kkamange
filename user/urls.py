from django.urls import path
from .adapters import NaverLogin

app_name = 'user'


urlpatterns = [
    path('login/naver/', NaverLogin.as_view(), name='naver_login')
]
