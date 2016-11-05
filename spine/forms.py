#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Spine


class SpineForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SpineForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Spine
