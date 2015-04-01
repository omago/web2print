#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import PaperWeight


class PaperWeightForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaperWeightForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PaperWeight
        exclude = ['slug']