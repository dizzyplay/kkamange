from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignupForm(UserCreationForm):
    nickname = forms.CharField(max_length=20)

    def save(self):
        user = super().save()

        Profile.objects.create(
            user=user,
            nickname=self.cleaned_data['nickname']
        )

        return user



