#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Product


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

    cutting_order = forms.IntegerField(label="Rezanje", required=False)
    improper_cutting_order = forms.IntegerField(label="Nepravilno rezanje", required=False)
    creasing_order = forms.IntegerField(label="Biganje", required=False)
    hole_drilling_order = forms.IntegerField(label="Bušenje rupa", required=False)
    vacuuming_order = forms.IntegerField(label="Vakumiranje", required=False)
    bindings_order = forms.IntegerField(label="Uvez", required=False)
    flexion_order = forms.IntegerField(label="Savijanje", required=False)
    laminating_order = forms.IntegerField(label="Laminiranje", required=False)
    plastic_order = forms.IntegerField(label="Plastika", required=False)
    rounding_order = forms.IntegerField(label="Rundanje", required=False)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Product
        exclude = ['slug']