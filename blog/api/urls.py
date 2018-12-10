from django.urls import re_path
from . import views

app_name = 'blog'


urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<post_pk>\d+)$', views.post_detail, name='post_detail'),
]