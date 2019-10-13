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
    LUNES = 'Lu'
    MARTES = 'Ma'
    MIERCOLES = 'Mi'
    JUEVES = 'Ju'
    VIERNES = 'Vi'

    DAYS_CHOICES = (
        (LUNES, 'Lunes'),
        (MARTES, 'Martes'),
        (MIERCOLES, 'Miercoles'),
        (JUEVES, 'Jueves'),
        (VIERNES, 'Viernes'),
    )
    workday = models.ForeignKey(
        Workday,
        on_delete=models.CASCADE,
        null=False,
        blank=False
        )
    day = models.CharField(
        max_length=12,
        choices=DAYS_CHOICES
        )
    start_time = models.TimeField()
    end_time = models.TimeField()

    
