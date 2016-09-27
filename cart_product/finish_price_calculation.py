#!/usr/bin/env python
# -*- coding: utf-8 -*-

from finish_price.models import FinishPrice
from decimal import *
from finish.models import Finish


class FinishPriceCalculation:

    def __init__(self, number_of_sheets, finishes, volume, product_format, number_of_copies, finish_model):
        self.number_of_sheets = number_of_sheets

        self.finishes = finishes
        self.volume = volume
        self.number_of_copies = number_of_copies
        self.finish_model = finish_model
        self.product_format = product_format
        self.affects_assembly_in_press = False

        self.total_finishes_price = 0
        #TODO: cijena papira, kako se izračunavai izračunav ali se za svaku doradu???

    def get_price(self):
        """
        Funkcija konvertira cijenu u float

        Returns:
            Funkcija vraća cijenu

        """
        return Decimal(self.total_finishes_price)

    def calculate_price(self):
        """
        Funkcija kojom se poziva izračun

        Returns:
            Funkcija ne vraća ništa, dodaje cijenu svake dorade na finish_price

        """
        if len(self.finishes) > 0:
            for finish in self.finishes:
                finish_price = self.get_finish_price(finish)
                if finish_price:
                    self.total_finishes_price += finish_price

    def get_finish_price(self, finish_dict):
        """
        Funkcija kojom se računa cijena za određenu doradu

        Returns:
            Funkcija vraća cijenu dorade

        """
        finish = None
        if "finish_id" in finish_dict:
            finish = self.finish_model.objects.get(pk=finish_dict["finish_id"])  #TODO provjeriti točnos finish_id-ija

        finish_type_id = None
        if "finish_type_id" in finish_dict:
            finish_type_id = finish_dict["finish_type_id"]
            if finish_type_id is None:
                return None

        # u slučaju da je na doradi određeno da dorada utječe na montažu postaviti za cijeli izračun da utječe na
        # montažu kako bi se vrijednosti vratila u glavni izračun
        if finish.finish.affects_assembly_in_press:
            self.affects_assembly_in_press = True

        if finish.finish.x == Finish.COPIES:
            x = self.number_of_copies
        elif finish.finish.x == Finish.NUMBER_OF_SHEETS:
            x = self.number_of_sheets
        else:
            x = self.number_of_copies  #TODO: ovo bi trebao biti izračun po kvadratu - potrebno provjeriti
            #TODO kod finish modela ne postoji definiranje cijene po kvadratu, dali se dobije finish.finish.x vrijednost


        # cijena se prvo dohvaća za fiksni x
        finish_price = FinishPrice.get_x_price(finish.id, x, finish_type_id)

        # ako je x nađen u bazi dodjeljuje se cijena iz baze
        if finish_price:
            x_price = finish_price.x_price
            start_price = finish_price.start_price
        else:
            a = FinishPrice.get_x_lt_price(finish.id, x, finish_type_id)
            b = FinishPrice.get_x_gt_price(finish.id, x, finish_type_id)

            if a and b:
                x_price = a.x_price - ((a.x_price - b.x_price) / (b.x - a.x)) * (x - a.x)
                start_price = a.start_price
            else:
                return None

        price = start_price + (x * x_price)

        return price

    #TODO zašto korisnik na kalkulatoru odabire papir kada može odabirati papir gramaturu i finish posebno,
    #TODO pisanje skripti za unos???