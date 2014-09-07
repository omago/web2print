#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Banner


class BannerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BannerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Banner
        exclude = ['slug']