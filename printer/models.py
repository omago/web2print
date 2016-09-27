#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from press.models import Press


class Printer(models.Model):
    SHEET = "QUIRE"
    COPIES = "COPIES"
    M2 = "M2"
    OFFSET = "OFFSET"

    printing_price_types_choices = (
        (SHEET, "ARAK"),
        (COPIES, "NAKLADA"),
        (M2, "KVADRATNI METAR"),
        (OFFSET, "OFFSET")
    )

    name = models.CharField(verbose_name="Naziv", max_length=512)
    color = models.BooleanField(verbose_name="Color")
    printing_area_width = models.IntegerField(verbose_name="Širina otiska")
    printing_area_height = models.IntegerField(verbose_name="Visina otiska")
    max_paper_width = models.IntegerField(verbose_name="Maksimalna širina papira")
    max_paper_height = models.IntegerField(verbose_name="Maksimalna visina papira")
    click_width = models.IntegerField(verbose_name="Širina klika")
    user_discount = models.BooleanField(verbose_name="Omogući korisnički popust")
    role = models.BooleanField(blank=True, verbose_name="Rola")
    paper_weight_payment_threshold = models.IntegerField(max_length=11, blank=True, null=True, verbose_name="Težina papira nakon koje se papir plaća")
    press = models.ManyToManyField(Press, verbose_name="Tisak", related_name="printer-press")
    printing_price_type = models.CharField(verbose_name="Vrsta izračuna cijene", max_length=128, choices=printing_price_types_choices)

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "printer"