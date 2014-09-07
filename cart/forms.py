#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Cart


class CartForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CartForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Cart
        exclude = ['product', 'cart']