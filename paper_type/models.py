#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class PaperType(models.Model):
    name = models.CharField(verbose_name="Naziv", max_length=1024)
    has_finish = models.BooleanField(verbose_name="Ima finish")
    better_quality_paper = models.BooleanField(verbose_name="Kvalitetniji papir")

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "paper_type"