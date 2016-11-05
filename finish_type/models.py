#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from finish.models import Finish


class FinishType(models.Model):
    finish = models.ForeignKey(Finish, verbose_name="Dorada")
    name = models.CharField(verbose_name="Naziv", max_length="1024")
    spine = models.BooleanField(verbose_name="Ima hrbat")
    weight = models.DecimalField(verbose_name="Težina dorade po m2", decimal_places=4, max_digits=11, null=True, blank=True)

    def __unicode__(self):
        return self.finish.name + " - " + self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "finish_type"

    @staticmethod
    def get(pk):
        return FinishType.objects.filter(pk=pk).first()
