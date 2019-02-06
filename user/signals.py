from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from user.models import Profile


@receiver(user_signed_up)
def user_signup(request, user, **kwargs):
    if len(user.socialaccount_set.all()) > 0:
        soccial_account = user.socialaccount_set.all()[0]
        gender = soccial_account.extra_data.get('gender', None)
        Profile.objects.create(user=user, nickname=user.username, gender=gender)
