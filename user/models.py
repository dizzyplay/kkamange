from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female'),
        ('not-specified','Not Specified')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.nickname

    def username(self):
        return self.user.username



