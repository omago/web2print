#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Press


class PressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PressForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Press
        exclude = ['slug']