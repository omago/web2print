#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from cart.models import Cart
from product.models import Product
from format.models import Format
from paper.models import Paper
from press.models import Press
from finish.models import Finish
from finish_type.models import FinishType


class CartProduct(models.Model):

    cart = models.ForeignKey(Cart, verbose_name="Košarica")
    product = models.ForeignKey(Product, verbose_name="Proizvod")

    title = models.CharField(max_length=1024, null=True, blank=True, verbose_name="Naslov")
    format = models.ForeignKey(Format, null=True, verbose_name="Format (ŠxV)", related_name="cart-product-format")
    paper = models.ForeignKey(Paper, null=True, verbose_name="Papir", related_name="cart-product-paper")
    press = models.ForeignKey(Press, null=True, verbose_name="Tisak", related_name="cart-product-press")
    number_of_copies = models.IntegerField(null=True, verbose_name="Naklada")

    number_of_mutation = models.IntegerField(null=True, blank=True, verbose_name="Broj mutacija")
    volume = models.IntegerField(null=True, blank=True, verbose_name="Opseg")

    has_cover = models.BooleanField(verbose_name="Korice")
    cover_paper = models.ForeignKey(Paper, null=True, blank=True, verbose_name="Papir za korice", related_name="cart-product-cover-paper")

    has_insert = models.BooleanField(verbose_name="Umetak")
    number_of_inserts = models.IntegerField(null=True, blank=True, verbose_name="Broj umetanja")
    has_insert_print = models.BooleanField(verbose_name="Tisak umetka")
    insert_paper = models.ForeignKey(Paper, null=True, blank=True, verbose_name="Papir na umetku", related_name="cart-product-insert-paper")
    insert_press = models.ForeignKey(Press, null=True, blank=True, verbose_name="Tisak umetka", related_name="cart-product-insert-press")
    insert_volume = models.IntegerField(null=True, blank=True, verbose_name="Opseg umetka")

    finish = models.ManyToManyField(Finish, verbose_name="Dorade", null=True, blank=True, related_name="cart-product-finish")
    finish_type = models.ManyToManyField(FinishType, verbose_name="Tipovi dorada", null=True, blank=True, related_name="cart-product-finish-type")

    class Meta:
        ordering = ['-pk']
        db_table = "cart_product"