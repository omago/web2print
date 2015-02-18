#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Flexion


class FlexionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FlexionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Flexion
        exclude = ['slug']