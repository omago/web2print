#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import NumberOfColors


class NumberOfColorsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NumberOfColorsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = NumberOfColors