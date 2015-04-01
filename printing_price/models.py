#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from printer.models import Printer


class PrintingPrice(models.Model):
    printer = models.ForeignKey(Printer, verbose_name="Stroj")
    quire_from = models.IntegerField(verbose_name="Broj araka od")
    quire_to = models.IntegerField(verbose_name="Broj araka do")
    start_price = models.DecimalField(verbose_name="Cijena starta", max_digits=11, decimal_places=2)
    click_price = models.DecimalField(verbose_name="Cijena klika", max_digits=11, decimal_places=2)
    both_sides_price = models.DecimalField(verbose_name="Cijena obostranog tiska", max_digits=11, decimal_places=2)

    def __unicode__(self):
        return self.start_price

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "printing_price"