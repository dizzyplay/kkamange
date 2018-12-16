from django.db import models
from django.contrib.auth import get_user_model
from blog.models import Post
from user.models import Profile


User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def nickname(self):
        return str(Profile.objects.get(id=self.user.id))

    def short_date(self):
        return self.created_at.strftime("%y-%m-%d")

    def children(self):
        return Comment.objects.filter(parent=self)

