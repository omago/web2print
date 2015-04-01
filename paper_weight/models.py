#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class PaperWeight(models.Model):
    weight = models.IntegerField(verbose_name="Gramatura")

    def __unicode__(self):
        return self.weight

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "paper_weight"