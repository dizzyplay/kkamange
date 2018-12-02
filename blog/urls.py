from django.urls import path
from . import views

app_name='blog'

urlpattenrs=[
    path('', views.main, name='main'),
]