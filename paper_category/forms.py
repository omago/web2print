#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import PaperCategory


class PaperCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaperCategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PaperCategory