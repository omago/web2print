#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Product
from finish.models import Finish


class ProductForm(forms.ModelForm):

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
        self.fields["printer"].widget.attrs.update({'size': '10'})
        self.fields["cover_printer"].widget.attrs.update({'size': '10'})
        self.fields["insert_printer"].widget.attrs.update({'size': '10'})

    class Meta:
        model = Product
        exclude = ['slug']
        widgets = {
            'formats': forms.CheckboxSelectMultiple(),
            'paper': forms.CheckboxSelectMultiple(),
            'press': forms.CheckboxSelectMultiple(),
            'cover_paper': forms.CheckboxSelectMultiple(),
            'cover_plastic': forms.CheckboxSelectMultiple(),
            'insert_paper': forms.CheckboxSelectMultiple(),
            'finish': forms.CheckboxSelectMultiple(),
            'finish_type': forms.CheckboxSelectMultiple(),
        }

    # def save(self, commit=True):
    #     instance = super(ProductForm, self).save(commit=False)
    #
    #     if commit:
    #         instance.save()
    #     return instance