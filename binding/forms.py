#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Binding


class BindingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BindingForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Binding
        exclude = ['slug']