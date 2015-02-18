#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Plastic


class PlasticForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PlasticForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Plastic
        exclude = ['slug']