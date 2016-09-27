#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms


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

    def get_row(self):
        finish_id = self.widget_id + "_" + str(self.finish.pk)
        finish_attributes = {"id": finish_id, "value": self.finish.pk}

        if self.is_finish_checked:
            finish_attributes["checked"] = "checked"

        main_checkbox = forms.CheckboxInput(attrs=finish_attributes).render(name=self.name, value=None)
        finish_type = self.get_finish_types()

        row = '<div>' \
              '<label for="' + finish_id + '">' + self.finish.finish.name + '</label>' + \
              '<div class="checkbox-select">' + main_checkbox + finish_type + '</div></div>'

        return row

    def get_finish_types(self):

        finish_type_string = ""
        finish_types = self.finish.finish_type.all()

        if len(finish_types) > 0:
            finish_type_list = [("", "---------")]
            finish_type_attributes = {}
            finish_type_name = self.widget_id + "-finish-type-" + str(self.finish.pk)
            finish_type_value = None

            if not self.is_finish_checked:
                finish_type_attributes["style"] = "display:none"

            for finish_type in finish_types:
                finish_type_list.append((finish_type.pk, finish_type.name))

            if self.data and finish_type_name in self.data:
                try:
                    finish_type_value = self.data[finish_type_name][0]
                except IndexError:
                    pass

            finish_type_field = forms.Select(choices=finish_type_list, attrs=finish_type_attributes)
            finish_type_string = finish_type_field.render(name=finish_type_name, value=finish_type_value)

        return finish_type_string

    def is_finish_checked(self):
        is_finish_checked = False
        if (self.value and self.finish.pk in self.value) or \
                (not self.value and self.finish.is_on):
            is_finish_checked = True

        return is_finish_checked

    def get_style(self):
        return 'style="display:none"' if self.is_finish_checked is False else ''