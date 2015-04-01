#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Plastic(models.Model):
    name = models.CharField(verbose_name="Naziv", max_length=1024)

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "plastic"