#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models, connection
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.shortcuts import get_object_or_404

from django.utils.translation import ugettext_lazy as _

from valuenetwork.valueaccounting.models import Location

class UseFaircoin(models.Model):
    name = models.CharField(_('name'), max_length=128, unique=True)
    description = models.TextField(_('description'), blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(default=0.0, blank=True, null=True)
    longitude = models.FloatField(default=0.0, blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name
