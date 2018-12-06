from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO
import sys


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def save(self):
        im = Image.open(self.photo)
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
        # imageField 값을 새롭게 수정된 이미지 값으로 변경
        self.photo = InMemoryUploadedFile(output, 'ImageField', '%s.jpg' % self.photo.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output),None)
        super(Post, self).save()
