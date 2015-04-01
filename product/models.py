#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify

from product_subcategory.models import ProductSubcategory
from format.models import Format
from paper.models import Paper
from press.models import Press
from plastic.models import Plastic
from binding.models import Binding
from flexion.models import Flexion


class Product(models.Model):

    # product attributes
    name = models.CharField(max_length=128, verbose_name="Naziv")
    subcategory = models.ForeignKey(ProductSubcategory, verbose_name="Podkategorija")
    slug = models.SlugField(max_length=128, verbose_name="Slug")
    image = models.ImageField(max_length=128, verbose_name="Slika", upload_to="products", null=True, blank=True)
    description = models.TextField(verbose_name="Opis", null=True, blank=True)

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

    # finishing attributes
    has_cutting = models.BooleanField(verbose_name="Proizvod ima rezanje")
    has_improper_cutting = models.BooleanField(verbose_name="Proizvod ima nepravilno rezanje")
    has_creasing = models.BooleanField(verbose_name="Proizvod ima biganje")
    has_hole_drilling = models.BooleanField(verbose_name="Proizvod ima bušenje rupa")
    has_vacuuming = models.BooleanField(verbose_name="Proizvod ima vakumiranje")
    has_binding = models.BooleanField(verbose_name="Proizvod ima uvez")
    bindings = models.ManyToManyField(Binding, verbose_name="Uvezi", null=True, related_name="product-bindings")
    has_flexion = models.BooleanField(verbose_name="Proizvod ima savijanje")
    flexion = models.ManyToManyField(Flexion, verbose_name="Savijanje", null=True, related_name="product-flexion")
    has_laminating = models.BooleanField(verbose_name="Proizvod ima laminiranje")
    has_plastic = models.BooleanField(verbose_name="Proizvod ima plastiku")
    plastic = models.ManyToManyField(Plastic, verbose_name="Plastika", related_name="product-plastic", null=True)
    has_rounding = models.BooleanField(verbose_name="Proizvod ima rundanje")

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