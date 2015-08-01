#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Product
from finish.models import Finish


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["cover_finish"].choices = self.get_cover_finish_choices()
        self.fields["finish"].choices = self.get_finish_choices()
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
            'printer': forms.CheckboxSelectMultiple(),
            'cover_paper': forms.CheckboxSelectMultiple(),
            'cover_printer': forms.CheckboxSelectMultiple(),
            'cover_finish': forms.CheckboxSelectMultiple(),
            'insert_press': forms.CheckboxSelectMultiple(),
            'insert_paper': forms.CheckboxSelectMultiple(),
            'insert_printer': forms.CheckboxSelectMultiple(),
            'finish': forms.CheckboxSelectMultiple(),
        }

    def save(self, commit=True):
        instance = super(ProductForm, self).save(commit=False)

        # ukloni polja da ih save_m2m metoda ne pokuša spremit
        del self.cleaned_data['cover_finish']
        del self.cleaned_data['cover_finish_type']
        del self.cleaned_data['finish']
        del self.cleaned_data['finish_type']

        if commit:
            instance.save()
        return instance

    def get_cover_finish_choices(self):

        cover_finish_list = []
        cover_finish_orders = []

        if self.instance.cover_finish_order:
            cover_finish_orders = self.instance.cover_finish_order.split(",")
            for cover_finish_order in cover_finish_orders:
                try:
                    cover_finish = Finish.objects.filter(cover=True).get(pk=int(cover_finish_order))
                    cover_finish_list.append((cover_finish.pk, cover_finish.name))
                except Finish.DoesNotExist:
                    pass

        cover_finishes = Finish.objects.filter(cover=True).exclude(pk__in=cover_finish_orders)

        for cover_finish in cover_finishes:
            cover_finish_list.append((cover_finish.pk, cover_finish.name))

        return cover_finish_list

    def get_finish_choices(self):

        finish_list = []
        finish_orders = []

        if self.instance.finish_order:
            finish_orders = self.instance.finish_order.split(",")
            for finish_order in finish_orders:
                try:
                    finish = Finish.objects.get(pk=int(finish_order))
                    finish_list.append((finish.pk, finish.name))
                except Finish.DoesNotExist:
                    pass

        finishes = Finish.objects.exclude(pk__in=finish_orders)

        for finish in finishes:
            finish_list.append((finish.pk, finish.name))

        return finish_list