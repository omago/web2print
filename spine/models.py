#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from finish_type.models import FinishType
from paper.models import Paper


class Spine(models.Model):
    finish_type = models.ForeignKey(FinishType, verbose_name="Tip dorade", related_name="spine-finish-type")
    paper = models.ForeignKey(Paper, verbose_name="Papir")
    thickness = models.DecimalField(verbose_name="Debljina", decimal_places=4, max_digits=11)
    number_of_pages_from = models.IntegerField(verbose_name="Broj stranica od")
    number_of_pages_to = models.IntegerField(verbose_name="Broj stranica do")

    def __unicode__(self):
        return self.number_of_pages_from

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "spine"
        unique_together = ('finish_type', 'paper', 'thickness', 'number_of_pages_from', 'number_of_pages_to')
        verbose_name = "Hrbat"
        verbose_name_plural = "Hrbati"
