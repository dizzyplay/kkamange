from allauth.account.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def user_login(request, user, **kwargs):
    print(user.__dict__)