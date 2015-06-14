#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from finish.models import Finish
from finish_type.models import FinishType


class FinishPrice(models.Model):
    finish = models.ForeignKey(Finish, verbose_name="Dorada")
    finish_type = models.ForeignKey(FinishType, verbose_name="Tip dorade", null=True, blank=True)
    x = models.IntegerField(verbose_name="X")
    start_price = models.DecimalField(verbose_name="Cijena starta", decimal_places=2, max_digits=11)
    x_price = models.DecimalField(verbose_name="Cijena X-a", decimal_places=2, max_digits=11)

    def __unicode__(self):
        return self.x_price

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "finish_price"