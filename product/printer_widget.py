#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'domagoj'

from django import forms
from printer.models import Printer
from django.forms import widgets
from django.utils.html import format_html

from product.models import ProductPrinter


class PrinterWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        self.data = None
        _widgets = ()
        super(PrinterWidget, self).__init__(_widgets, attrs)

    def render(self, name, value, attrs=None):

        widget_id = attrs["id"]
        printer_list = []
        i = 0

        for printer in self.choices.queryset:
            printer_id = widget_id + "_" + str(i)

            select_name = "printing-price-type-" + str(printer.pk)
            printer_attrs = {"id": printer_id, "value": printer.pk}
            select_value = self.get_select_value(printer, select_name)

            if value and printer.pk in value:
                printer_attrs["checked"] = "checked"

            checkbox = forms.CheckboxInput(attrs=printer_attrs).render(name=name, value=None)
            select = forms.Select(choices=Printer.printing_price_types_choices).render(name=select_name, value=select_value)
            printer_list.append('<li><label for="' + printer_id + '">' + checkbox + printer.name + select + '</label></li>')
            i += 1

        return format_html('<ul class="checkbox-select" id="' + widget_id + '">' + "".join(printer_list) + "</ul>")

    def value_from_datadict(self, data, files, name):
        self.data = data
        return_values = []

        values = data.getlist(name)
        for value in values:
            printer = int(value)
            return_values.append(printer)

        return return_values

    def get_select_value(self, printer, select_name):

        select_value = printer.printing_price_type

        if self.data:
            select_value = self.data.get(select_name)
        elif self.attrs["product"]:
            try:
                product_printer = ProductPrinter.objects.filter(product=self.attrs["product"], printer=printer).get()
                select_value = product_printer.printing_price_type
            except ProductPrinter.DoesNotExist:
                pass

        return select_value
