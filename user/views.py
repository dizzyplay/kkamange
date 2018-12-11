from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.views import LoginView
from .forms import SignupForm
from .serializer import UserSerializer, ProfileSerializer

User = get_user_model()


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, './user/sign_up_form.html', {
        'form': form
    })


class CustomLoginView(LoginView):
    template_name = './user/login.html'


login = CustomLoginView.as_view()


def logout_view(request):
    logout(request)
    return redirect('/')


def jwt_response_payload_handler(token, user=None, request=None):
    profile = user.profile_set.get(user=user)
    serializer = ProfileSerializer(profile)
    return {
        'token': token,
        'profile':serializer.data
    }
