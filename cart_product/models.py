#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.validators import MinValueValidator


from django.db import models
from cart.models import Cart
from product.models import Product
from product_format.models import ProductFormat
from number_of_colors.models import NumberOfColors

class CartProduct(models.Model):

    cart = models.ForeignKey(Cart, verbose_name="Košarica")
    product = models.ForeignKey(Product, verbose_name="Proizvod")
    number_of_pages = models.PositiveIntegerField(validators=[MinValueValidator(1)], null=True, verbose_name="Broj stranica")
    product_format = models.ForeignKey(ProductFormat, null=True, verbose_name="Format (ŠxV)")
    number_of_colors = models.ForeignKey(NumberOfColors, null=True, verbose_name="Broj boja")
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], null=True, verbose_name="Količina")
    plastic_finish = models.BooleanField(verbose_name="Dorada plastika")
    uv_finish = models.BooleanField(verbose_name="Dorada UV lak")

    class Meta:
        ordering = ['-pk']
        db_table = "cart"