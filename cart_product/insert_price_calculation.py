#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *
from insert_price.models import InsertPrice
from .printing_price_calculation import PrintingPriceCalculation


class InsertPriceCalculation:

    def __init__(self, user, has_insert, number_of_copies, number_of_inserts, insert_print, insert_paper, insert_press,
                 insert_volume, product_format):
        self.user = user
        self.product_format = product_format
        self.number_of_copies = number_of_copies

        self.has_insert = has_insert
        self.number_of_insert_copies = number_of_copies * number_of_inserts  #TODO dali je ovo točno? Broj kopija je jednako broj kopija
        self.number_of_inserts = number_of_inserts
        self.insert_print = insert_print
        self.insert_paper = insert_paper
        self.insert_press = insert_press
        self.insert_volume = insert_volume

        self.total_insert_price = Decimal(0)

    def get_price(self):
        """
        Funkcija konvertira cijenu u float

        Returns:
            Funkcija vraća cijenu

        """
        return Decimal(self.total_insert_price)

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
        if self.has_insert and self.number_of_inserts and self.number_of_copies:
            self.total_insert_price += self.get_insert_price()

            # ako je potreban tisak umetka, ako je odabran papir, vrsta tiska, i opseg
            if self.insert_print and self.insert_paper and self.insert_press and self.insert_volume:
                self.total_insert_price += self.get_insert_print_price()

        return self.get_price()

    def get_insert_price(self):
        """
        Funkcija nalazi cijenu  umetanja umetka.
            1. Cijena umetanja - računa se po formuli start + (naklada * broj_umetanja * cijena_po_umetku)

        Returns:
            Funkcija vraća cijenu i stroj

        """
        insert_price = Decimal(0)

        try:
            insert_price_object = InsertPrice.objects\
                .filter(number_of_inserts_per_copy=self.number_of_inserts)\
                .get()
            insert_price = insert_price_object.start_price + (self.number_of_insert_copies *
                                                              insert_price_object.price_per_insert)
        except InsertPrice.DoesNotExist:
            pass

        return insert_price

    def get_insert_print_price(self):
        """
        Funkcija nalazi tiska umetka, zove se izračun cijene tiska s parametrima.

        Returns:
            Funkcija vraća cijenu i stroj

        """
        #TODO do kraja definriait cijenu tiska umetka!!!
        return PrintingPriceCalculation(printers=self.product.printer.all(),  #TODO koji su printeri za umetak
                                        user=self.user,  #TODO ima li korisnik nekakve popuste na tisak umetka
                                        finish_affects_assembly_in_press=False,  #TODO može li dorada utjecati an cijenu umetka?
                                        product_format=self.product_format,
                                        press=self.insert_press,
                                        paper=self.insert_paper,
                                        number_of_copies=self.number_of_insert_copies,
                                        number_of_mutation=number_of_mutation,  #TODO koji je broj mutacija za umetak, 1?
                                        volume=self.insert_volume)
