from django.urls import path
from . import views

app_name = 'user'


urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout')
]
