#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify


class ArticleCategory(models.Model):
    name = models.CharField(max_length=128, verbose_name="Naziv")
    slug = models.SlugField(max_length=128, verbose_name="Slug")
    description = models.TextField(verbose_name="Opis", null=True, blank=True)
    meta_description = models.TextField(verbose_name="Meta opis", null=True, blank=True)
    meta_keywords = models.TextField(verbose_name="Ključne riječi", null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ArticleCategory, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']
        db_table = "article_category"