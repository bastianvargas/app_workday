# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class workday(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    schedule = models.TextField()
    
