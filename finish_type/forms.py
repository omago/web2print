#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import FinishType
from finish.models import Finish


class FinishTypeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FinishTypeForm, self).__init__(*args, **kwargs)
        self.fields['finish'].queryset = Finish.objects.filter(has_types=True)

    class Meta:
        model = FinishType


class FinishTypeSearchForm(forms.Form):

    finish = forms.ModelChoiceField(Finish.objects.filter(has_types=True), label="Dorada", required=False)

    def __init__(self, *args, **kwargs):
        super(FinishTypeSearchForm, self).__init__(*args, **kwargs)

