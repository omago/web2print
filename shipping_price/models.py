#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class ShippingPrice(models.Model):
    weight_from = models.IntegerField(verbose_name="Težina od (g)")
    weight_to = models.IntegerField(verbose_name="Težina do (g)")
    price = models.DecimalField(verbose_name="Cijena", decimal_places=4, max_digits=11)

    def __unicode__(self):
        return self.price

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "shipping_price"
        unique_together = ('weight_from', 'weight_to')
        verbose_name = "Cijena dostave"
        verbose_name_plural = "Cijene dostave"