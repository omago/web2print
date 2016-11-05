#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import ShippingPrice


class ShippingPriceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ShippingPriceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ShippingPrice