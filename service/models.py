#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from service_category.models import ServiceCategory

class Service(models.Model):
    name = models.CharField(max_length=128, verbose_name="Naziv")
    service_category = models.ForeignKey(ServiceCategory, verbose_name="Kategorija usluge")

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "service"