from django.db import models
from django.utils.html import mark_safe
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO
import sys


# Create your models here.
def resize_mini_photo(img):
    im = Image.open(img)
    output = BytesIO()
    width, height = im.size
    if width > height:
        left = (width - height) /2
        top = 0
        right = left + height
        bottom = height
    elif width < height:
        left = 0
        top = (height - width) /2
        right = width
        bottom = top + height
    else:
        left = 0
        top = 0
        right = width
        bottom = height

    size = (left, top, right, bottom)
    im_crop = im.crop(size)
    im_crop = im_crop.resize((64,64), Image.ANTIALIAS)
    im_crop.save(output, format='JPEG', quality=80)
    return output


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
        im = Image.open(self.photo)
        mini_output = resize_mini_photo(self.photo)
        exif = im._getexif()
        output = BytesIO()
        image_width = 1280
        x = image_width
        y = round((im.size[1]/im.size[0]) * image_width)  # 가로비율만큼 세로비율 줄임
        im = im.resize((x, y))

        # 아이폰에서 직접 사진을 찍어 올리면 가로로 눕는현상 때문에 exif 확인 후 rotate
        orientation_key = 274  # Exif 태그
        if exif and orientation_key in exif:
            orientation = exif[orientation_key]
            rotate_values = {
                3: Image.ROTATE_180,
                6: Image.ROTATE_270,
                8: Image.ROTATE_90
            }
            if orientation in rotate_values:
                im = im.transpose(rotate_values[orientation])

        im.save(output, format="JPEG", quality=80)
        output.seek(0)
        mini_output.seek(0)
        # imageField 값을 새롭게 수정된 이미지 값으로 변경
        self.photo = InMemoryUploadedFile(output, 'ImageField', '%s.jpg' % self.photo.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output),None)
        self.thumbnail = InMemoryUploadedFile(mini_output, 'ImageField',
                                              '%s_thumbnail.jpg'% self.photo.name.split('.')[0],
                                              'image/jpeg', sys.getsizeof(mini_output),None)
        super(Post, self).save()


