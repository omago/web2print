#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from paper_category.models import PaperCategory

class PaperType(models.Model):
    name = models.CharField(max_length=128, verbose_name="Naziv")
    weight = models.IntegerField(verbose_name="Gramatura")
    paper_category = models.ForeignKey(PaperCategory, verbose_name="Kategorija papira")

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "paper_type"