#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cart_product.calculators.printing_price_calculation import PrintingPriceCalculation

from cart_product.calculators.finish_price_calculation import FinishPriceCalculation
from cart_product.calculators.insert_price_calculation import InsertPriceCalculation
from cart_product.calculators.price_calculation_helper import PriceCalculationHelper
from cart_product.calculators.weight_calculation import WeightCalculation
from format.models import Format
from paper.models import Paper
from press.models import Press
from product.models import Product
from product.models import ProductFinish
from .cover_price_calculation import CoverPriceCalculation


class PriceCalculation:

    def __init__(self, data, user):

        self.data = data  # POST data
        self.user = user  # trenutni korisnik

        self.calculation_helper = PriceCalculationHelper(self.data)

        self.product = self.calculation_helper.get_object_by_pk(Product, "product")  # odabrani proizvod

        # parametri tiska
        self.product_format = self.calculation_helper.get_object_by_pk(Format, "format_choices")  # format papira
        self.paper = self.calculation_helper.get_object_by_pk(Paper, "paper")  # odabrani papir
        self.number_of_copies = self.calculation_helper.get_value_from_data("number_of_copies", int, 0)  # naklada - broj primjeraka
        self.number_of_mutation = self.calculation_helper.get_value_from_data("number_of_mutation", int, 1)  # broj mutacija
        self.volume = self.calculation_helper.get_value_from_data("volume", int, 0)  # broj stranica
        self.press = self.calculation_helper.get_object_by_pk(Press, "press")  # odabrani tisak
        self.number_of_copies = self.calculation_helper.get_value_from_data("number_of_copies", int, 0)  # naklada - broj primjeraka
        self.number_of_mutation = self.calculation_helper.get_value_from_data("number_of_mutation", int, 1)  # broj mutacija
        self.volume = self.calculation_helper.get_value_from_data("volume", int, 0)  # broj stranica

        self.printing_price = 0
        self.printing_printer = None
        self.number_of_sheets = 0  # broj araka

        # parametri umetka
        self.has_insert = self.calculation_helper.get_value_from_data("has_insert")  # ima umetak
        self.number_of_inserts = self.calculation_helper.get_value_from_data("number_of_inserts", int, 0)  # broj umetaka
        self.insert_print = self.calculation_helper.get_value_from_data("insert_print")  # ima umetak
        self.insert_paper = self.calculation_helper.get_object_by_pk(Paper, "insert_paper")  # papir umetka
        self.insert_press = self.calculation_helper.get_object_by_pk(Press, "insert_press")  # tiska umetka
        self.insert_volume = self.calculation_helper.get_value_from_data("insert_volume", int, 0)  # opseg umetka

        self.insert_price = 0
        self.insert_printer = None
        self.number_of_insert_copies = self.number_of_inserts * self.number_of_copies

        # parametri korica
        self.has_cover = self.calculation_helper.get_value_from_data("has_cover")  # ima korice
        self.cover_paper = self.calculation_helper.get_object_by_pk(Paper, "cover_paper")  # papir korica
        self.cover_finishes = self.calculation_helper.get_finishes("cover_finish")  # dorade za korice

        self.cover_price = 0

        # parametri dorade
        self.finishes = self.calculation_helper.get_finishes("finish")  # dorade
        self.finish_price = 0
        self.finish_affects_assembly_in_press = self.calculation_helper.does_finish_affect_assembly_in_press(self.finishes)

        # cijena finalnog proizvoda
        self.product_price = 0

        # parametri težine proizvoda
        self.book_block_weight = 0
        self.insert_weight = 0
        self.cover_weight = 0

        self.product_weight = 0

        # širina hrbta
        #TODO: izračunati širinu hrbta prema debljini papira, papir ima debljinu u mm i pomnožiti s brojem strana

        # TODO: napraviti košaricu do kraja i istestirati, napraviti korisnički račun na frontendu gdje korisnik može vidjeti svoje narudžbe

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
        self.printing_price = self.get_printing_price()
        self.finish_price = FinishPriceCalculation(self, self.finishes, ProductFinish).calculate_price()
        self.cover_price = CoverPriceCalculation(self, cover_finishes=self.cover_finishes).calculate_price()

        InsertPriceCalculation(self).calculate_price()
        WeightCalculation(self).calculate_product_weight()

        self.product_price = self.printing_price + self.insert_price + self.cover_price + self.finish_price

    def get_printing_price(self):
        """
        Funkcija poziva calculator dorada te dohvaća cijenu

        Returns:
            funkcija vraća cijenu koju vrati kalkulator

        """
        printing_calculation = PrintingPriceCalculation(printers=self.product.printer.all(),
                                                        user=self.user,
                                                        finish_affects_assembly_in_press=self.finish_affects_assembly_in_press,
                                                        product_format=self.product_format,
                                                        press=self.press,
                                                        paper=self.paper,
                                                        number_of_copies=self.number_of_copies,
                                                        number_of_mutation=self.number_of_mutation,
                                                        volume=self.volume)
        price = printing_calculation.calculate_price()
        self.number_of_sheets = printing_calculation.number_of_sheets

        return price