#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Binding(models.Model):
    name = models.CharField(verbose_name="Naziv", max_length=1024)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "binding"