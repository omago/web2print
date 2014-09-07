#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import CartProduct


class CartProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CartProductForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CartProduct
        exclude = ['slug']