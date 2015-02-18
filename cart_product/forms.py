#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import CartProduct
from product_format.models import ProductFormat
from paper.models import Paper
from press.models import Press
from plastic.models import Plastic
from binding.models import Binding
from flexion.models import Flexion


class CartProductForm(forms.ModelForm):

    def __init__(self, product, *args, **kwargs):
        super(CartProductForm, self).__init__(*args, **kwargs)

        self.fields.keyOrder = []

        if not product.has_title:
            self.fields.pop('title')
        else:
            self.fields.keyOrder.append('title')

        self.fields.keyOrder.append('format')
        self.fields["format"].queryset = ProductFormat.objects.filter(pk__in=product.product_formats.all())
        self.fields.keyOrder.append('paper')
        self.fields["paper"].queryset = Paper.objects.filter(pk__in=product.paper.all())
        self.fields.keyOrder.append('press')
        self.fields["press"].queryset = Press.objects.filter(pk__in=product.press.all())
        self.fields.keyOrder.append('number_of_copies')

        if not product.has_mutations:
            self.fields.pop('number_of_mutation')
        else:
            self.fields.keyOrder.append('number_of_mutation')

        if not product.has_cover:
            self.fields.pop('cover_paper')
            self.fields.pop('cover_plastic')
        else:
            self.fields.keyOrder.append('cover_paper')
            self.fields["cover_paper"].queryset = Paper.objects.filter(pk__in=product.cover_paper.all())
            self.fields.keyOrder.append('cover_plastic')
            self.fields["cover_plastic"].queryset = Plastic.objects.filter(pk__in=product.cover_plastic.all())

        if not product.has_insert:
            self.fields.pop('insert_paper')
        else:
            self.fields.keyOrder.append('insert_paper')
            self.fields["insert_paper"].queryset = Paper.objects.filter(pk__in=product.insert_paper.all())

        #
        # DORADE
        #
        if not product.has_cutting:
            self.fields.pop('cutting')
        else:
            self.fields.keyOrder.append('cutting')

        if not product.has_improper_cutting:
            self.fields.pop('improper_cutting')
        else:
            self.fields.keyOrder.append('improper_cutting')

        if not product.has_creasing:
            self.fields.pop('creasing')
        else:
            self.fields.keyOrder.append('creasing')

        if not product.has_hole_drilling:
            self.fields.pop('hole_drilling')
        else:
            self.fields.keyOrder.append('hole_drilling')

        if not product.has_vacuuming:
            self.fields.pop('vacuuming')
        else:
            self.fields.keyOrder.append('vacuuming')

        if not product.has_binding:
            self.fields.pop('bindings')
        else:
            self.fields.keyOrder.append('bindings')
            self.fields["bindings"].queryset = Binding.objects.filter(pk__in=product.bindings.all())

        if not product.has_flexion:
            self.fields.pop('flexion')
        else:
            self.fields.keyOrder.append('flexion')
            self.fields["flexion"].queryset = Flexion.objects.filter(pk__in=product.flexion.all())

        if not product.has_laminating:
            self.fields.pop('laminating')
        else:
            self.fields.keyOrder.append('laminating')

        if not product.has_plastic:
            self.fields.pop('plastic')
        else:
            self.fields.keyOrder.append('plastic')
            self.fields["plastic"].queryset = Plastic.objects.filter(pk__in=product.plastic.all())

        if not product.has_rounding:
            self.fields.pop('rounding')
        else:
            self.fields.keyOrder.append('rounding')

    class Meta:
        model = CartProduct
        exclude = ['slug']