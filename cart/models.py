#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from user.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="Korisnik")

    class Meta:
        ordering = ['-pk']
        db_table = "cart"