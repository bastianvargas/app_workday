# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Workday(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    workday = models.ForeignKey(
        Workday,
        on_delete=models.CASCADE,
        null=False,
        blank=False
        )
    day = models.CharField(max_length=15)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
