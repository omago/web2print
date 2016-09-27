#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from paper_type.models import PaperType
from paper_finish.models import PaperFinish
from paper_weight.models import PaperWeight


class Paper(models.Model):
    paper_type = models.ForeignKey(PaperType, verbose_name="Tip papira")
    paper_weight = models.ForeignKey(PaperWeight, verbose_name="Gramatura papira")
    paper_finish = models.ForeignKey(PaperFinish, verbose_name="Finish papira", blank=True, null=True)
    paper_thickness = models.DecimalField(decimal_places=4, max_digits=11, verbose_name="Debljina papira")
    price_per_kilogram = models.DecimalField(decimal_places=4, max_digits=11, null=True, blank=True, verbose_name="Cijena po kilogramu")
    role = models.BooleanField(blank=True, verbose_name="Rola")
    price_per_kilogram_role = models.DecimalField(decimal_places=4, max_digits=11, null=True, blank=True, verbose_name="Cijena po kilogramu (rola)")

    def __unicode__(self):

        paper_name = str(self.paper_weight.weight) + "g/m2 " + self.paper_type.name

        if self.paper_finish:
            paper_name += " " + self.paper_finish.name

        return paper_name

    def get_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    class Meta:
        ordering = ['-pk']
        db_table = "paper"
