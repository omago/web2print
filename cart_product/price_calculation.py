#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *

from product.models import Product
from paper.models import Paper
from press.models import Press
from format.models import Format
from product.models import ProductFinish

from .price_calculation_helper import PriceCalculationHelper
from .finish_price_calculation import FinishPriceCalculation
from .cover_price_calculation import CoverPriceCalculation
from .insert_price_calculation import InsertPriceCalculation
from .printing_price_calculation import PrintingPriceCalculation


class PriceCalculation:

    def __init__(self, data, user):

        self.data = data  # POST data
        self.user = user  # trenutni korisnik

        self.calculation_helper = PriceCalculationHelper(self.data)

        self.product = self.calculation_helper.get_object_by_pk(Product, "product")  # odabrani proizvod

        # zajednički parametri
        self.product_format = self.calculation_helper.get_object_by_pk(Format, "format_choices")  # format papira
        self.number_of_copies = self.calculation_helper.get_value_from_data("number_of_copies", int, 0)  # naklada - broj primjeraka
        self.number_of_mutation = self.calculation_helper.get_value_from_data("number_of_mutation", int, 1)  # broj mutacija
        self.volume = self.calculation_helper.get_value_from_data("volume", int, 0)  # broj stranica

        # parametri tiska
        self.printing_price = 0
        self.printing_printer = None
        self.number_of_sheets = 0  # broj araka

        # parametri umetka
        self.insert_price = 0
        self.insert_printer = None

        # parametri korica
        self.cover_price = 0

        # parametri dorade
        self.finish_price = 0
        self.finish_affects_assembly_in_press = False

        # cijena finalnog proizvoda
        self.product_price = 0

        # todo izračunati težinu proizvoda, težina papira puta naklada, puta broj kopija, puta opseg itd
        # todo istestirati košaricu

    def get_price(self):
        """
        Funkcija konvertira cijenu u Decimal

        Returns:
            Funkcija vraća cijenu

        """
        return float(self.product_price)

    def calculate_price(self):
        """
        Glavni handler izračuna

        Returns:
            izračunava cijenu

        """
        self.finish_price = self.get_finish_price()
        self.printing_price = self.get_printing_price()
        self.insert_price = self.get_insert_price()
        self.cover_price = self.get_cover_price()

        self.product_price = self.printing_price + self.insert_price + self.cover_price + self.finish_price

    def get_printing_price(self):
        """
        Funkcija poziva calculator dorada te dohvaća cijenu

        Returns:
            funkcija vraća cijenu koju vrati kalkulator

        """
        press = self.calculation_helper.get_object_by_pk(Press, "press")  # odabrani tisak
        paper = self.calculation_helper.get_object_by_pk(Paper, "paper")  # odabrani papir
        number_of_copies = self.calculation_helper.get_value_from_data("number_of_copies", int, 0)  # naklada - broj primjeraka
        number_of_mutation = self.calculation_helper.get_value_from_data("number_of_mutation", int, 1)  # broj mutacija
        volume = self.calculation_helper.get_value_from_data("volume", int, 0)  # broj stranica

        printing_calculation = PrintingPriceCalculation(printers=self.product.printer.all(),
                                                        user=self.user,
                                                        finish_affects_assembly_in_press=self.finish_affects_assembly_in_press,
                                                        product_format=self.product_format,
                                                        press=press,
                                                        paper=paper,
                                                        number_of_copies=number_of_copies,
                                                        number_of_mutation=number_of_mutation,
                                                        volume=volume)
        printing_calculation.calculate_price()
        self.number_of_sheets = printing_calculation.number_of_sheets

        return printing_calculation.get_price()

    def get_insert_price(self):
        """
        Funkcija poziva calculator umetka te dohvaća cijenu

        Returns:
            funkcija vraća cijenu koju vrati kalkulator

        """
        has_insert = self.calculation_helper.get_value_from_data("has_insert")  # ima umetak
        number_of_inserts = self.calculation_helper.get_value_from_data("number_of_inserts", int, 0)  # broj umetaka
        insert_print = self.calculation_helper.get_value_from_data("insert_print")  # ima umetak
        insert_paper = self.calculation_helper.get_object_by_pk(Paper, "insert_paper")  # papir umetka
        insert_press = self.calculation_helper.get_object_by_pk(Press, "insert_press")  # tiska umetka
        insert_volume = self.calculation_helper.get_value_from_data("insert_volume", int, 0)  # opseg umetka

        insert_calculation = InsertPriceCalculation(has_insert=has_insert,
                                                    user=self.user,
                                                    number_of_copies=self.number_of_copies,
                                                    number_of_inserts=number_of_inserts,
                                                    insert_print=insert_print,
                                                    insert_paper=insert_paper,
                                                    insert_press=insert_press,
                                                    insert_volume=insert_volume,
                                                    product_format=self.product_format)
        insert_calculation.calculate_price()
        return insert_calculation.get_price()

    def get_cover_price(self):
        """
        Funkcija poziva calculator korica te dohvaća cijenu

        Returns:
            funkcija vraća cijenu koju vrati kalkulator

        """
        has_cover = self.calculation_helper.get_value_from_data("has_cover")  # ima korice
        cover_paper = self.calculation_helper.get_object_by_pk(Paper, "cover_paper")  # papir korica
        cover_finishes = self.calculation_helper.get_finishes("cover_finish")  # dorade za korice

        cover_calculation = CoverPriceCalculation(volume=self.volume, product_format=self.product_format,
                                                  number_of_copies=self.number_of_copies, has_cover=has_cover,
                                                  cover_paper=cover_paper, cover_finishes=cover_finishes)
        cover_calculation.calculate_price()
        return cover_calculation.get_price()

    def get_finish_price(self):
        """
        Funkcija poziva calculator dorada te dohvaća cijenu

        Returns:
            funkcija vraća cijenu koju vrati kalkulator

        """
        finishes = self.calculation_helper.get_finishes("finish")  # dorade
        finish_calculation = FinishPriceCalculation(finishes=finishes,
                                                    volume=self.volume,
                                                    product_format=self.product_format,
                                                    number_of_copies=self.number_of_copies,
                                                    finish_model=ProductFinish)
        finish_calculation.calculate_price()
        self.finish_affects_assembly_in_press = finish_calculation.affects_assembly_in_press

        return finish_calculation.get_price()
