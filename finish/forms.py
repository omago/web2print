#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Finish


class FinishForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FinishForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Finish
