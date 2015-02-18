#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Paper


class PaperForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaperForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Paper
        exclude = ['slug']