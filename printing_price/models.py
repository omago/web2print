#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from printer.models import Printer


class PrintingPrice(models.Model):
    printer = models.ForeignKey(Printer, verbose_name="Stroj")
    both_sides = models.BooleanField(verbose_name="Obostrani tisak")
    x = models.IntegerField(verbose_name="X")
    start_price = models.DecimalField(verbose_name="Cijena starta", null=True, blank=True, max_digits=11, decimal_places=4)
    start_price_per_sheet = models.DecimalField(verbose_name="Cijena starta po arku", null=True, blank=True, max_digits=11, decimal_places=4)
    x_price = models.DecimalField(verbose_name="Cijena x-a", max_digits=11, decimal_places=4)
    printing_price_type = models.CharField(verbose_name="Vrsta izračuna cijene", max_length=128, choices=Printer.printing_price_types_choices)
    minimum_price = models.DecimalField(verbose_name="Minimalna cijena", max_digits=11, decimal_places=4, null=True, blank=True)

    def __unicode__(self):
        return self.start_price

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "printing_price"
        verbose_name = "Cijena printa"
        verbose_name_plural = "Cijene printa"
        unique_together = ('printer', 'both_sides', 'x', 'printing_price_type')

    @staticmethod
    def get_x_price(printer, both_sides, x):
        try:
            printing_price = PrintingPrice.objects\
                .filter(printer_id=printer.id)\
                .filter(printing_price_type=printer.printing_price_type)\
                .filter(both_sides=both_sides)\
                .filter(x=x)\
                .get()
        except PrintingPrice.DoesNotExist:
            printing_price = None

        return printing_price

    @staticmethod
    def get_x_lt_price(printer, both_sides, x):
        try:
            printing_price = PrintingPrice.objects\
                .filter(printer_id=printer.id)\
                .filter(printing_price_type=printer.printing_price_type)\
                .filter(both_sides=both_sides)\
                .filter(x__lt=x)\
                .order_by('-x')\
                .first()
        except PrintingPrice.DoesNotExist:
            printing_price = None

        return printing_price

    @staticmethod
    def get_x_gt_price(printer, both_sides, x):
        try:
            printing_price = PrintingPrice.objects\
                .filter(printer_id=printer.id)\
                .filter(printing_price_type=printer.printing_price_type)\
                .filter(both_sides=both_sides)\
                .filter(x__gt=x)\
                .order_by('x')\
                .first()
        except PrintingPrice.DoesNotExist:
            printing_price = None

        return printing_price