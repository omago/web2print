#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify

from product_subcategory.models import ProductSubcategory
from format.models import Format
from paper.models import Paper
from press.models import Press
from plastic.models import Plastic
from finish.models import Finish
from finish_type.models import FinishType
from printer.models import Printer


class Product(models.Model):

    # product attributes
    name = models.CharField(max_length=128, verbose_name="Naziv")
    subcategory = models.ForeignKey(ProductSubcategory, verbose_name="Podkategorija")
    slug = models.SlugField(max_length=128, verbose_name="Slug")
    image = models.ImageField(max_length=128, verbose_name="Slika", upload_to="products", null=True, blank=True)
    description = models.TextField(verbose_name="Opis", null=True, blank=True)
    printer = models.ManyToManyField(Printer, verbose_name="Stroj", null=True, blank=True)

    # base attributes
    has_title = models.BooleanField(verbose_name="Proizvod ima naslov")
    formats = models.ManyToManyField(Format, null=True, verbose_name="Formati proizvoda", related_name="product-formats")
    paper = models.ManyToManyField(Paper, related_name="paper", null=True, verbose_name="Papiri")
    press = models.ManyToManyField(Press, verbose_name="Tisak", null=True)
    has_mutations = models.BooleanField(verbose_name="Proizvod ima mutacije")
    has_cover = models.BooleanField(verbose_name="Proizvod ima korice")
    cover_paper = models.ManyToManyField(Paper, verbose_name="Papiri za korice", null=True)
    cover_plastic = models.ManyToManyField(Plastic, verbose_name="Platika za korice", null=True)
    has_insert = models.BooleanField(verbose_name="Proizvod ima umetak")
    insert_paper = models.ManyToManyField(Paper, verbose_name="Papiri za umetke", null=True, related_name="product-insert-paper")
    insert_press = models.ManyToManyField(Press, verbose_name="Tisak za umetak", null=True, related_name="product-insert-press")

    #finish
    finish = models.ManyToManyField(Finish, verbose_name="Dorade", null=True, blank=True)
    finish_type = models.ManyToManyField(FinishType, verbose_name="Tipovi dorada", null=True, blank=True)
    finish_order = models.CharField(verbose_name="Redoslijed dorada", max_length=1024, null=True, blank=True)

    # meta attributes
    meta_description = models.TextField(verbose_name="Meta opis", null=True, blank=True)
    meta_keywords = models.TextField(verbose_name="Ključne riječi", null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']
        db_table = "product"