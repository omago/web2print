#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from printer.models import Printer


class PrintingPrice(models.Model):
    printer = models.ForeignKey(Printer, verbose_name="Stroj")
    both_sides = models.BooleanField(verbose_name="Obostrani tisak")
    x = models.IntegerField(verbose_name="X")
    start_price = models.DecimalField(verbose_name="Cijena starta", max_digits=11, decimal_places=4)
    x_price = models.DecimalField(verbose_name="Cijena x-a", max_digits=11, decimal_places=4)

    def __unicode__(self):
        return self.start_price

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "printing_price"