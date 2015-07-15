#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import InsertPrice


class InsertPriceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InsertPriceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = InsertPrice