#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Product
from finish.models import Finish


class ProductForm(forms.ModelForm):

    title_order = forms.IntegerField(label="Naslov", required=False)
    format_order = forms.IntegerField(label="Format", required=False)
    paper_order = forms.IntegerField(label="Papir", required=False)
    press_order = forms.IntegerField(label="Tisak", required=False)
    number_of_mutations_order = forms.IntegerField(label="Broj mutacija", required=False)
    number_of_copies_order = forms.IntegerField(label="Naklada", required=False)
    cover_paper_order = forms.IntegerField(label="Papir za korice", required=False)
    cover_plastic_order = forms.IntegerField(label="Plastika za korice", required=False)
    insert_paper_order = forms.IntegerField(label="Papir za umetak", required=False)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        finish_list = []
        if self.instance.finish_order:
            finish_orders = self.instance.finish_order.split(",")
            for finish_order in finish_orders:
                finish = Finish.objects.get(pk=int(finish_order))
                finish_list.append((finish.pk, finish.name))

            finishes = Finish.objects.exclude(pk__in=finish_orders)

            for finish in finishes:
                finish_list.append((finish.pk, finish.name))

            self.fields["finish"].choices = finish_list

    class Meta:
        model = Product
        exclude = ['slug']
        widgets = {
            'finish': forms.CheckboxSelectMultiple(),
            'finish_type': forms.CheckboxSelectMultiple(),
        }

    # def save(self, commit=True):
    #     instance = super(ProductForm, self).save(commit=False)
    #
    #     if commit:
    #         instance.save()
    #     return instance