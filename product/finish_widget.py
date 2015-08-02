#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import widgets
from django.utils.html import format_html
from finish.models import Finish
from finish_widget_helper import FinishWidgetHelper


class FinishWidget(widgets.MultiWidget):
    def __init__(self, attrs=None, order=None, cover=None):
        self.data = None
        self.order = order
        _widgets = ()
        super(FinishWidget, self).__init__(_widgets, attrs)

    def render(self, name, value, attrs=None):

        widget_id = attrs["id"]
        finish_rows = []
        finish_orders = []

        if self.attrs["order"] and self.attrs["product"] and hasattr(self.attrs["product"], self.attrs["order"]):
            finish_orders = getattr(self.attrs["product"], self.attrs["order"]).split(",")
            for finish_order in finish_orders:
                try:
                    finish = Finish.objects
                    if "cover" in self.attrs and self.attrs["cover"]:
                        finish = finish.filter(cover=True)
                    finish = finish.get(pk=int(finish_order))
                    row = FinishWidgetHelper(widget_id=widget_id, data=self.data, value=value, name=name, finish=finish,
                                             product=self.attrs["product"], model=self.attrs["model"]).get_row()

                    finish_rows.append(row)
                except Finish.DoesNotExist:
                    pass

        finishes = Finish.objects
        if "cover" in self.attrs and self.attrs["cover"]:
            finishes = finishes.filter(cover=True)
        finishes = finishes.exclude(pk__in=finish_orders)

        for finish in finishes:
            row = FinishWidgetHelper(widget_id=widget_id, data=self.data, value=value, name=name, finish=finish,
                                     product=self.attrs["product"], model=self.attrs["model"]).get_row()

            finish_rows.append(row)

        return format_html('<ul id="' + widget_id + '" class="checkbox-select" id="' + widget_id + '">' + "".join(finish_rows) + "</ul>")

    def value_from_datadict(self, data, files, name):
        self.data = data
        return_values = []

        values = data.getlist(name)
        for value in values:
            finish = int(value)
            return_values.append(finish)

        return return_values