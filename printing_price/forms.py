#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import PrintingPrice


class PrintingPriceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PrintingPriceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PrintingPrice
        exclude = ['slug']