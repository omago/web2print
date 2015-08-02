#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from press.models import Press


class Printer(models.Model):

    printing_price_types_choices = (
        ("QUIRE", "ARAK"),
        ("COPIES", "NAKLADA"),
        ("M2", "KVADRATNI METAR")
    )

    name = models.CharField(verbose_name="Naziv", max_length=512)
    color = models.BooleanField(verbose_name="Color")
    width = models.IntegerField(verbose_name="Širina printa")
    height = models.IntegerField(verbose_name="Visina printa")
    user_discount = models.BooleanField(verbose_name="Omogući korisnički popust")
    role = models.BooleanField(blank=True, verbose_name="Rola")
    press = models.ManyToManyField(Press, verbose_name="Tisak", related_name="printer-press")
    printing_price_type = models.CharField(verbose_name="Vrsta izračuna cijene", max_length=128, choices=printing_price_types_choices)

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "printer"