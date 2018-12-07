from django.db import models
from django.utils.html import mark_safe
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

from .image_processor import resize_mini_photo, resize_and_rotate


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='image/%Y/%m/%d')
    thumbnail = models.ImageField(upload_to='thumbnail/%Y/%m/%d', editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def image_tag(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.photo.url))

    def save(self):
        output = resize_and_rotate(self.photo)
        thumbnail_output = resize_mini_photo(self.photo)
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
