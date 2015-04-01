#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Format


class FormatForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormatForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Format
        exclude = ['slug']