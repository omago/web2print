#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import PaperType


class PaperTypeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaperTypeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PaperType