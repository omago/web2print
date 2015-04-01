#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import PaperFinish


class PaperFinishForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaperFinishForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PaperFinish
        exclude = ['slug']