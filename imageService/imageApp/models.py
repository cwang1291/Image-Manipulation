# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Image(models.Model):
    data = models.ImageField(upload_to = 'pictures')
    image_type = models.CharField(max_length=30)
    image_size = models.IntegerField()
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


