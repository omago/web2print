#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import widgets
from django.utils.html import format_html
from finish.models import Finish
from django import forms
from cart_product.finish_widget_helper import FinishWidgetHelper


class FinishWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        self.data = None
        self.order = None
        self.product = None
        self.model = None
        _widgets = ()
        super(FinishWidget, self).__init__(_widgets, attrs)

    def render(self, name, value, attrs=None):
        self.set_attributes()

        widget_id = attrs["id"]
        finish_rows = []

        if self.attrs["order"] and self.attrs["product"] and hasattr(self.attrs["product"], self.attrs["order"]):
            finish_ids = getattr(self.attrs["product"], self.attrs["order"]).split(",")
            for finish_id in finish_ids:
                try:
                    finish = self.attrs["model"].objects\
                        .filter(product=self.product)\
                        .filter(finish_id=finish_id)\
                        .get()

                    row = FinishWidgetHelper(widget_id=widget_id, data=self.data, value=value, name=name, finish=finish,
                                             product=self.product, model=self.model).get_row()

                    finish_rows.append(row)

                except self.model.DoesNotExist:
                    pass

        return format_html("".join(finish_rows))

    def set_attributes(self):
        self.product = self.attrs["product"]
        self.model = self.attrs["model"]
        self.order = getattr(self.attrs["product"], self.attrs["order"]).split(",")

    def value_from_datadict(self, data, files, name):
        self.data = data
        return_values = []

        values = data.getlist(name)
        for value in values:
            finish = int(value)
            return_values.append(finish)

        return return_values