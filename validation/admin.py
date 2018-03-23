# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from validation.models import *


class ValidationAdmin(admin.ModelAdmin):
    list_display = ('event', 'validated_by', 'validation_date')

admin.site.register(Validation, ValidationAdmin)
