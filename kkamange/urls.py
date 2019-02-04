"""kkamange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from graphene_django.views import GraphQLView

from .social import NaverLogin

urlpatterns = [
    # django rest framework jwt api
    # path('api-token-auth/', obtain_jwt_token),
    # path('api-token-verify/', verify_jwt_token),

    # all auth
    re_path(r'^accounts/', include('allauth.urls')),

    # rest auth
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^rest-auth/naver/$', NaverLogin.as_view(), name='nv_login'),

    # api

    path('blog/api/', include('blog.api.urls', namespace='blog_api')),
    path('comment/api/', include('comment.api.urls', namespace='comment_api')),

    # django urls
    path('user/', include('user.urls', namespace='user')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),

    # graphql
    re_path(r'^graphql/$', GraphQLView.as_view(graphiql=True)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
