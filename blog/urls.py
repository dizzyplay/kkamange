from django.urls import path, re_path
from . import views

app_name='blog'

urlpatterns=[
    path('', views.main, name='main'),
    path('new/', views.post_new, name='post_new'),
    # graphql
]