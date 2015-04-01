#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from cart.models import Cart
from product.models import Product
from format.models import Format
from paper.models import Paper
from press.models import Press
from plastic.models import Plastic
from binding.models import Binding
from flexion.models import Flexion


class CartProduct(models.Model):

    cart = models.ForeignKey(Cart, verbose_name="Košarica")
    product = models.ForeignKey(Product, verbose_name="Proizvod")

    title = models.CharField(max_length=1024, null=True, blank=True, verbose_name="Naslov")
    format = models.ForeignKey(Format, null=True, verbose_name="Format (ŠxV)", related_name="cart-product-format")
    paper = models.ForeignKey(Paper, null=True, verbose_name="Papir", related_name="cart-product-paper")
    press = models.ForeignKey(Press, null=True, verbose_name="Tisak", related_name="cart-product-press")
    number_of_copies = models.IntegerField(null=True, verbose_name="Naklada")
    number_of_mutation = models.IntegerField(null=True, blank=True, verbose_name="Broj mutacija")
    cover_paper = models.ForeignKey(Paper, null=True, blank=True, verbose_name="Papir za korice", related_name="cart-product-cover-paper")
    cover_plastic = models.ForeignKey(Plastic, null=True, blank=True, verbose_name="Plastika na koricama", related_name="cart-product-cover-plastic")
    insert_paper = models.ForeignKey(Paper, null=True, blank=True, verbose_name="Papir na umetku", related_name="cart-product-insert-paper")

    cutting = models.BooleanField(verbose_name="Rezanje")
    improper_cutting = models.BooleanField(verbose_name="Nepravilno rezanje")
    creasing = models.BooleanField(verbose_name="Biganje")
    hole_drilling = models.BooleanField(verbose_name="Bušenje rupa")
    vacuuming = models.BooleanField(verbose_name="Vakumiranje")
    bindings = models.ForeignKey(Binding, verbose_name="Uvez", blank=True, null=True)
    flexion = models.ForeignKey(Flexion, verbose_name="Savijanje", blank=True, null=True)
    laminating = models.BooleanField(verbose_name="Laminiranje")
    plastic = models.ForeignKey(Plastic, verbose_name="Plastika", related_name="cart-product-plastic", blank=True, null=True)
    rounding = models.BooleanField(verbose_name="Rundanje")

    class Meta:
        ordering = ['-pk']
        db_table = "cart_product"