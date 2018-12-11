from django.db import models
from django.utils.html import mark_safe
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth import get_user_model
import sys

from .image_processor import make_thumbnail, resize_and_rotate_img


User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='image/%Y/%m/%d')
    thumbnail = models.ImageField(upload_to='thumbnail/%Y/%m/%d', editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.photo.url))

    def comment_count(self):
        return self.comment_set.all().count()

    def short_date(self):
        return self.created_at.strftime('%y년 %m월 %d일 %H시 %m분')


    def save(self):
        output = resize_and_rotate_img(self.photo)
        thumbnail_output = make_thumbnail(self.photo)
        output.seek(0)
        thumbnail_output.seek(0)
        # imageField 값을 새롭게 수정된 이미지 값으로 변경
        self.photo = InMemoryUploadedFile(output, 'ImageField', '%s.jpg' % self.photo.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)
        # thumbnail 저장
        self.thumbnail = InMemoryUploadedFile(thumbnail_output, 'ImageField',
                                              '%s_thumbnail.jpg' % self.photo.name.split('.')[0],
                                              'image/jpeg', sys.getsizeof(thumbnail_output), None)
        super(Post, self).save()
