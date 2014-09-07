#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify


class BannerPosition(models.Model):
    name = models.CharField(max_length=128, verbose_name="Naziv")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['pk']
        db_table = "banner_position"