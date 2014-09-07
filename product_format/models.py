#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class ProductFormat(models.Model):
    width = models.IntegerField(verbose_name="Širina")
    height = models.IntegerField(verbose_name="Visina")

    def __unicode__(self):
        return str(self.width) + "x" + str(self.height)

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "product_format"