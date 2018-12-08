from PIL import Image
from io import BytesIO


def rotate_img(img):
    im = Image.open(img)
    try:
        exif = im._getexif()
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
    except AttributeError:
        # exif 정보가 존재하지 않음
        pass

    return im


def make_thumbnail(img):
    im = rotate_img(img)
    output = BytesIO()
    width, height = im.size
    if width > height:
        left = (width - height) / 2
        top = 0
        right = left + height
        bottom = height
    elif width < height:
        left = 0
        top = (height - width) / 2
        right = width
        bottom = top + width
    else:
        left = 0
        top = 0
        right = width
        bottom = height

    size = (left, top, right, bottom)
    im_crop = im.crop(size)
    im_crop = im_crop.resize((64, 64), Image.ANTIALIAS)
    im_crop.save(output, format='JPEG', quality=80)

    return output


def resize_and_rotate_img(img):
    im = rotate_img(img)
    output = BytesIO()
    image_width = 1280
    x = image_width
    y = round((im.size[1]/im.size[0]) * image_width)  # 가로비율만큼 세로비율 줄임
    im = im.resize((x, y))
    im.save(output, format="JPEG", quality=80)

    return output
