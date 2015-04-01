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
    price_per_kilogram = models.DecimalField(decimal_places=2, max_digits=11, verbose_name="Cijena po kilogramu")

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