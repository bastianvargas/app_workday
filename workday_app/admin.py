# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Schedule, Workday

admin.site.register(Schedule)
admin.site.register(Workday)
