#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *
from printer_price_calculation import PrinterPriceCalculation


class PrintingPriceCalculation:

    def __init__(self, printers, product_format, press, paper, number_of_copies, volume, user, number_of_mutation=1,
                 finish_affects_assembly_in_press=False):

        # obavezni attributi
        self.printers = printers
        self.product_format = product_format
        self.press = press
        self.paper = paper

        # veličina proizvoda
        self.product_width = self.product_format.width
        self.product_height = self.product_format.height

        # podaci o količini
        self.number_of_copies = number_of_copies
        self.number_of_mutation = number_of_mutation
        self.volume = volume

        # utječe li dorada na cijenu tiska
        self.finish_affects_assembly_in_press = finish_affects_assembly_in_press

        # korisnik
        self.user = user

        # rezultat izračuna
        self.most_affordable_printer = None
        self.total_printing_price = 0
        self.number_of_sheets = 0

    def calculate_price(self):
        """
        Funkcija kojom se poziva izračun

        Returns:
            Funkcija ne vraća ništa, dodaje cijenu svake dorade na finish_price

        """
        if self.printers and self.product_format and self.press and self.paper and self.number_of_copies > 0:
            self.total_printing_price += self.get_printing_price()

        return Decimal(self.total_printing_price)

    def get_printing_price(self):
        """
        Funkcija nalazi cijenu naisplativijeg tiska.
        Prolazi korz printere definirane te računa cijenu za svaki od tih strojeva i vraća najnižu cijenu

        Returns:
            Funkcija vraća cijenu i printer

        """
        printing_price = 0

        for printer in self.printers:
            printer_price_calculation = PrinterPriceCalculation(printer=printer,
                                                                product_format=self.product_format,
                                                                press=self.press,
                                                                paper=self.paper,
                                                                number_of_copies=self.number_of_copies,
                                                                number_of_mutations=self.number_of_mutation,
                                                                volume=self.volume,
                                                                user=self.user,
                                                                finish_affects_assembly_in_press=self.finish_affects_assembly_in_press)

            printer_price = printer_price_calculation.calculate_price()
            number_of_sheets = printer_price_calculation.number_of_sheets

            if printer_price and (product_price == 0 or printer_price < product_price):
                product_price = printer_price
                self.most_affordable_printer = printer
                self.number_of_sheets = number_of_sheets

        return printing_price
