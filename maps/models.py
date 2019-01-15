#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models, connection
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.shortcuts import get_object_or_404

from django.utils.translation import ugettext_lazy as _

#from valuenetwork.valueaccounting.models import Location

class UseFaircoin(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True, null=True)
    tagline = models.CharField(_('tagline'), max_length=255, blank=True, null=True)
    description = models.TextField(_('description'), blank=True, null=True)
    address = models.CharField(_('address'), max_length=255, blank=True, null=True)
    hours = models.CharField(_('hours'), max_length=255, blank=True, null=True)
    phone = models.CharField(_('phone'), max_length=128, blank=True, null=True)
    website = models.CharField(_('website'), max_length=255, blank=True, null=True)
    twitter = models.CharField(_('twitter'), max_length=255, blank=True, null=True)
    faircoin_address = models.CharField(_('faircoin_address'), max_length=128, unique=True, blank=True, null=True)
    lat = models.FloatField(_('Latitude'), default=0.0, blank=True, null=True)
    lng = models.FloatField(_('Longitude'), default=0.0, blank=True, null=True)
    image = models.CharField(_('image'), max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title
