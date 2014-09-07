#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import ServiceCategory


class ServiceCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServiceCategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ServiceCategory