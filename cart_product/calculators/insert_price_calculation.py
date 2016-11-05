#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cart_product.calculators.printing_price_calculation import PrintingPriceCalculation
from insert_price.models import InsertPrice
from printer.models import Printer


class InsertPriceCalculation:

    def __init__(self, params):
        self.params = params

    def calculate_price(self):
        """
        Funkcija kojom se poziva izračun

        Returns:
            Funkcija vraća cijenu umetka, dodaje komponente cijene na total_insert_price
            Cijena se sastoji od dvije komponente:
            1. cijena umetanja
            2. tisak umetka

        """
        # ako proizvod ima umetak ima broj umetaka i nakladu
        if self.params.has_insert and self.params.number_of_inserts and self.params.number_of_copies:
            self.calculate_insert_price()

            # ako je potreban tisak umetka, ako je odabran papir, vrsta tiska, i opseg
            if self.params.insert_print and self.params.insert_paper and self.params.insert_press and \
                    self.params.insert_volume:
                self.params.insert_price += self.get_insert_print_price()

    def calculate_insert_price(self):
        """
        Funkcija nalazi cijenu  umetanja umetka.
            1. Cijena umetanja - računa se po formuli start + (naklada * broj_umetanja * cijena_po_umetku)

        Returns:
            Funkcija vraća cijenu

        """
        insert_price = InsertPrice.get(self.params.number_of_inserts)
        if insert_price:
            self.params.insert_price += insert_price.start_price + \
                (self.params.number_of_copies * self.params.number_of_inserts * insert_price.price_per_insert)

    def get_insert_print_price(self):
        """
        Funkcija nalazi tiska umetka, zove se izračun cijene tiska s parametrima.

        Returns:
            Funkcija vraća cijenu i stroj

        """
        calculation = PrintingPriceCalculation(printers=Printer.objects.all(),
                                               user=self.params.user,
                                               product_format=self.params.product_format,
                                               press=self.params.insert_press,
                                               paper=self.params.insert_paper,
                                               number_of_copies=self.params.number_of_insert_copies,
                                               volume=self.params.insert_volume)

        return calculation.calculate_price()
