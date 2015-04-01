#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from user.models import User
from product_subcategory.models import ProductSubcategory


class Format(models.Model):
    width = models.IntegerField(verbose_name="Širina")
    height = models.IntegerField(verbose_name="Visina")
    user = models.ForeignKey(User, verbose_name="Korisnik", blank=True, null=True)
    user_format = models.BooleanField(verbose_name="Korisnikov format")
    product_subcategory = models.ForeignKey(ProductSubcategory, verbose_name="Podkategorija proizvoda", blank=True, null=True)

    def __unicode__(self):
        return str(self.width) + "x" + str(self.height)

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "format"