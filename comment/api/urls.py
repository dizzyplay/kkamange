from django.urls import re_path
from . import views

app_name = 'comment'

urlpatterns =[
    re_path(r'^(?P<post_id>\d+)/$', views.comment_list, name="comment_list"),
]