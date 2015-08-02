#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from finish_type.models import FinishType


class FinishWidgetHelper():

    def __init__(self, widget_id, data, value, name, finish, product, model):
        self.widget_id = widget_id
        self.data = data
        self.value = value
        self.name = name
        self.finish = finish
        self.product = product
        self.model = model
        self.is_finish_checked = self.is_finish_checked()
        self.product_finish = self.get_product_finish(finish)

    def get_row(self):
        finish_id = self.widget_id + "_" + str(self.finish.pk)
        finish_attributes = {"id": finish_id, "value": self.finish.pk}

        if self.is_finish_checked:
            finish_attributes["checked"] = "checked"

        main_checkbox = forms.CheckboxInput(attrs=finish_attributes).render(name=self.name, value=None)
        is_on = self.get_is_on_checkbox()
        finish_type = self.get_finish_types()

        row = '<li><label for="' + finish_id + '">' + main_checkbox + self.finish.name + is_on + finish_type + '</label></li>'

        return row

    def get_is_on_checkbox(self):
        is_on_name = self.widget_id + "-finish-is-on-" + str(self.finish.pk)
        is_on_attributes = {"id": is_on_name}

        if self.data:
            if self.data.get(is_on_name) == "on":
                is_on_attributes["checked"] = "checked"
        elif self.product_finish and self.product_finish.is_on:
            is_on_attributes["checked"] = "checked"

        is_on_checkbox = forms.CheckboxInput(attrs=is_on_attributes).render(name=is_on_name, value=None)
        is_on_label = u"Označi kao uključeno"
        style = self.get_style()
        is_on = '<label ' + style + ' for="' + is_on_name + '">' + is_on_checkbox + is_on_label + '</label>'

        return is_on

    def get_finish_types(self):

        finish_type_string = ""
        finish_type_checkboxes = []
        finish_types = FinishType.objects.filter(finish=self.finish)
        for finish_type in finish_types:
            finish_type_id = self.widget_id + "-finish-type-" + str(finish_type.pk)
            finish_type_name = self.widget_id + "-finish-type-" + str(self.finish.pk)
            finish_type_attributes = {"id": finish_type_id, "value": finish_type.pk}

            if self.data:
                value = self.data.getlist(finish_type_name)
                if value and str(finish_type.pk) in value:
                    finish_type_attributes["checked"] = "checked"
            elif self.product_finish and finish_type in self.product_finish.finish_type.all():
                finish_type_attributes["checked"] = "checked"

            finish_type_checkbox = forms.CheckboxInput(attrs=finish_type_attributes).render(name=finish_type_name, value=None)
            finish_type_row = '<li><label for="' + finish_type_id + '">' + finish_type_checkbox + finish_type.name + '</label></li>'
            finish_type_checkboxes.append(finish_type_row)

        if len(finish_type_checkboxes) > 0:
            style = self.get_style()
            finish_type_string = '<ul ' + style + '>' + "".join(finish_type_checkboxes) + '</ul>'

        return finish_type_string

    def get_product_finish(self, finish):
        product_finish = None
        if self.product:
            try:
                product_finish = self.model.objects.get(finish=finish, product=self.product)
            except self.model.DoesNotExist:
                pass

        return product_finish

    def is_finish_checked(self):
        is_finish_checked = False
        if self.value and self.finish.pk in self.value:
            is_finish_checked = True

        return is_finish_checked

    def get_style(self):
        return 'style="display:none!important"' if self.is_finish_checked is False else ''