# This module contain a
# class of a Resizer, that
# allow to change size of an
# image loaded by a user.

from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile
from django.db import models



class ResizeImageMixin:
   """
      Class of a Resizer, that contain
      one method that handle image loaded
      size.
   """
   
   def resize(self, imageField:models.ImageField, size:tuple, emp_name):
      im = Image.open(imageField)
      source_image = im.convert('RGB')
      source_image.thumbnail(size)
      output = BytesIO()
      source_image.save(output, format='JPEG')
      output.seek(0)

      content_file = ContentFile(output.read())
      file = File(content_file)

      file_name = f'{emp_name}.jpeg'

      imageField.save(file_name, file, save=False)

