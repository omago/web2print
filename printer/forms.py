#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Printer


class PrinterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PrinterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Printer
        exclude = ['slug']