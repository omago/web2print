#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify

from product_subcategory.models import ProductSubcategory
from format.models import Format
from paper.models import Paper
from press.models import Press
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
    printer = models.ManyToManyField(Printer, verbose_name="Stroj", through="ProductPrinter", related_name="product-printer")

    # base attributes
    has_title = models.BooleanField(verbose_name="Proizvod ima naslov")
    formats = models.ManyToManyField(Format, null=True, verbose_name="Formati proizvoda", related_name="product_formats")
    paper = models.ManyToManyField(Paper, related_name="paper", null=True, verbose_name="Papiri")
    press = models.ManyToManyField(Press, verbose_name="Tisak", null=True)
    has_mutations = models.BooleanField(verbose_name="Proizvod ima mutacije")
    has_volume = models.BooleanField(verbose_name="Proizvod ima opseg")

    has_cover = models.BooleanField(verbose_name="Proizvod ima korice")
    turn_on_cover = models.BooleanField(verbose_name="Uključi korice")
    cover_paper = models.ManyToManyField(Paper, verbose_name="Papiri za korice", null=True, blank=True)
    cover_printer = models.ManyToManyField(Printer, verbose_name="Stroj za korice", null=True, blank=True, related_name="product-cover-printer")
    cover_finish = models.ManyToManyField(Finish, verbose_name="Dorade za korice", null=True, blank=True, through="ProductCoverFinish", related_name="product-cover-finish")
    cover_finish_type = models.ManyToManyField(FinishType, verbose_name="Tipovi dorada za korice", null=True, blank=True, related_name="product_cover_finish_type")
    cover_finish_order = models.CharField(verbose_name="Redoslijed dorada za korice", max_length=1024, null=True, blank=True)

    has_insert = models.BooleanField(verbose_name="Proizvod ima umetak")
    insert_paper = models.ManyToManyField(Paper, verbose_name="Papiri za umetke", null=True, blank=True, related_name="product-insert-paper")
    insert_press = models.ManyToManyField(Press, verbose_name="Tisak za umetak", null=True, blank=True, related_name="product-insert-press")
    insert_printer = models.ManyToManyField(Printer, verbose_name="Stroj za umetak", null=True, blank=True, related_name="product-insert-printer")

    #finish
    finish = models.ManyToManyField(Finish, verbose_name="Dorade", null=True, blank=True, through="ProductFinish", related_name="product-finish")
    finish_order = models.CharField(verbose_name="Redoslijed dorada", max_length=1024, null=True, blank=True)

    # meta attributes
    meta_description = models.TextField(verbose_name="Meta opis", null=True, blank=True)
    meta_keywords = models.TextField(verbose_name="Ključne riječi", null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    def save_finishes(self, request):
        ProductFinish.objects.filter(product=self).delete()
        finishes = request.POST.getlist('finish')

        for finish in finishes:
            finish_object = Finish.objects.get(pk=int(finish))
            is_on_name = "id_finish-finish-is-on-" + str(finish_object.pk)
            is_on = True if request.POST.get(is_on_name) == "on" else False
            finish_type_name = "id_finish-finish-type-" + str(finish_object.pk)

            product_finish = ProductFinish(finish=finish_object, product=self, is_on=is_on)
            product_finish.save()
            product_finish.finish_type.remove()

            values = request.POST.getlist(finish_type_name)

            for value in values:
                product_finish.finish_type.add(FinishType.objects.get(pk=int(value)))

    def save_cover_finishes(self, request):
        ProductCoverFinish.objects.filter(product=self).delete()
        finishes = request.POST.getlist('cover_finish')

        for finish in finishes:
            finish_object = Finish.objects.get(pk=int(finish))
            is_on_name = "id_cover_finish-finish-is-on-" + str(finish_object.pk)
            is_on = True if request.POST.get(is_on_name) == "on" else False
            finish_type_name = "id_cover_finish-finish-type-" + str(finish_object.pk)

            product_finish = ProductCoverFinish(finish=finish_object, product=self, is_on=is_on)
            product_finish.save()
            product_finish.finish_type.remove()

            values = request.POST.getlist(finish_type_name)

            for value in values:
                product_finish.finish_type.add(FinishType.objects.get(pk=int(value)))

    def save_printers(self, request):
        ProductPrinter.objects.filter(product=self).delete()
        printers = request.POST.getlist('printer')

        for printer in printers:
            printer_object = Printer.objects.get(pk=int(printer))

            select_name = "printing-price-type-" + str(printer_object.pk)
            minimum_name = "printing-price-minimum-" + str(printer_object.pk)

            printing_price_type = request.POST.get(select_name)
            minimum = request.POST.get(minimum_name)
            if minimum == "":
                minimum = 0

            ProductPrinter(printer=printer_object,
                           product=self,
                           printing_price_type=printing_price_type,
                           minimum=minimum)\
                .save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']
        db_table = "product"


class ProductFinish(models.Model):
    product = models.ForeignKey(Product)
    finish = models.ForeignKey(Finish)
    is_on = models.BooleanField()
    finish_type = models.ManyToManyField(FinishType)


class ProductCoverFinish(models.Model):
    product = models.ForeignKey(Product)
    finish = models.ForeignKey(Finish)
    is_on = models.BooleanField()
    finish_type = models.ManyToManyField(FinishType)


class ProductPrinter(models.Model):
    product = models.ForeignKey(Product)
    printer = models.ForeignKey(Printer)
    printing_price_type = models.CharField(max_length=128, choices=Printer.printing_price_types_choices)
    minimum = models.IntegerField()