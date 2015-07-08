#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import FinishPrice
from finish_type.models import FinishType
from finish.models import Finish


class FinishPriceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FinishPriceForm, self).__init__(*args, **kwargs)
        if kwargs and "initial" in kwargs:
            self.fields['finish_type'].queryset = FinishType.objects.filter(finish=kwargs["initial"]["finish"])
        elif args and args[0]["finish"]:
            self.fields['finish_type'].queryset = FinishType.objects.filter(finish=args[0]["finish"])
        elif self.instance.pk:
            if self.instance.finish:
                self.fields['finish_type'].queryset = FinishType.objects.filter(finish=self.instance.finish)
        else:
            self.fields['finish_type'].queryset = FinishType.objects.none()

    class Meta:
        model = FinishPrice


class FinishPriceSearchForm(forms.Form):

    finish = forms.ModelChoiceField(Finish.objects.all(), label="Dorada", required=False)
    finish_type = forms.ModelChoiceField(FinishType.objects.none(), label="Tip dorade", required=False)

    def __init__(self, *args, **kwargs):
        finish = kwargs.pop('finish', None)
        super(FinishPriceSearchForm, self).__init__(*args, **kwargs)

        if finish:
            self.fields['finish_type'].queryset = FinishType.objects.filter(finish=finish)