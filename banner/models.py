#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify

from banner_position.models import BannerPosition

class Banner(models.Model):
    name = models.CharField(max_length=128, verbose_name="Naziv")
    link = models.CharField(max_length=1024, verbose_name="Link")
    banner_position = models.ForeignKey(BannerPosition, verbose_name="Pozicija")
    image = models.ImageField(max_length=128, verbose_name="Slika", upload_to="banners")

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Banner, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']
        db_table = "banner"