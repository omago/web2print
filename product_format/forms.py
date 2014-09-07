#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import ProductFormat


class ProductFormatForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductFormatForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ProductFormat
        exclude = ['slug']