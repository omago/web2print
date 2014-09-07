#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Service