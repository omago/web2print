#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PriceCalculationHelper():

    def __init__(self, data):
        self.data = data

    def get_object_by_pk(self, model, key):
        """
        Funkcija traži objekt u bazi za primljeni model i key koji se nalazi u POST-u.

        Returns:
            Funkcija vraća objekt iz baze

        """
        object_id = self.get_value_from_data(key=key)
        object_from_db = None

        if object_id:
            object_from_db = model.objects.get(pk=object_id)

        return object_from_db

    def get_value_from_data(self, key, value_type=None, default=None):
        """
        Funkcija traži podatak u POST-u.

        Returns:
            Funkcija vraća vrijednost podatka

        """
        if value_type == list:
            value = self.data.getlist(key, None)
        else:
            value = self.data.get(key, None)

        if default and not value or value == "":
            value = default

        if value:
            if value_type and value_type == int:
                value = int(value)

        return value

    def get_finishes(self, key):
        """
        Funkcija traži dorade u POST-u.

        Returns:
            Funkcija vraća listu dorada za traženi key (finish, cover_finish)

        """
        finishes = self.get_value_from_data(key, list)
        finishes_list = []
        if len(finishes) > 0:
            for finish in finishes:
                finish_dict = {"finish_id": int(finish)}
                finish_type_key = "id_" + key + "-finish-type-" + finish
                if finish_type_key in self.data.keys():
                    finish_dict["finish_type_id"] = self.get_value_from_data(finish_type_key, int)

                finishes_list.append(finish_dict)

        return finishes_list