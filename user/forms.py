from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from allauth.account.forms import SignupForm as allauthSignupForm


class SignupForm(UserCreationForm):
    nickname = forms.CharField(max_length=20)

    def save(self):
        user = super().save()
        Profile.objects.create(
            user=user,
            nickname=self.cleaned_data['nickname']
        )
        return user


class CustomSignupForm(allauthSignupForm):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('not-specified','Not Specified')
    )
    nickname = forms.CharField(max_length=100)
    gender= forms.ChoiceField(choices=GENDER_CHOICES)

    def save(self, request):
        user = super().save(request)
        user_profile= Profile(user=user, nickname=self.cleaned_data['nickname'], gender=self.cleaned_data['gender'])
        user_profile.save()
        return user


