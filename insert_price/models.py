#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class InsertPrice(models.Model):
    start_price = models.DecimalField(verbose_name="Cijena starta", decimal_places=4, max_digits=11)
    number_of_inserts_per_copy = models.IntegerField(verbose_name="Broj umetanja po jedinici naklade")
    price_per_insert = models.DecimalField(verbose_name="Cijena umetanja", decimal_places=4, max_digits=11)

    def __unicode__(self):
        return self.start_price

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "insert_price"
        unique_together = ('start_price', 'number_of_inserts_per_copy', 'price_per_insert')
        verbose_name = "Cijena umetka"
        verbose_name_plural = "Cijene umetka"