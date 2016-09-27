#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Finish(models.Model):
    COPIES = "COPIES"
    NUMBER_OF_SHEETS = "NUMBER_OF_SHEETS"

    x_types = (
        (COPIES, "Naklada"),
        (NUMBER_OF_SHEETS, "Broj araka")
    )

    name = models.CharField(verbose_name="Naziv", max_length=1024)
    cover = models.BooleanField(verbose_name="Dorada za korice")
    x = models.CharField(verbose_name="Vrsta x-a", max_length=1024, choices=x_types)
    has_types = models.BooleanField(verbose_name="Sadrži tipove")
    display_as_additional = models.BooleanField(verbose_name="Prikaži kao dodatno na kalkulatoru")
    affects_assembly_in_press = models.BooleanField(verbose_name="Utječe na montažu u tisku")

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "finish"