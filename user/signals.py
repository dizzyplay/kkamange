from allauth.account.signals import user_logged_in, user_logged_out
from django.dispatch import receiver


@receiver(user_logged_in)
def user_login(request, user, **kwargs):
    print(request)
