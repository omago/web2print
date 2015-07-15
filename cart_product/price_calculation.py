#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from decimal import *

from product.models import Product
from paper.models import Paper
from press.models import Press
from printing_price.models import PrintingPrice
from insert_price.models import InsertPrice
from format.models import Format


class PriceCalculation():

    padding = 2  # napust kod printa
    paper_weight_payment_threshold = 250  # težina papira nakon koje se plaća i papir

    def __init__(self, user, product, paper, press, number_of_copies, paper_format,
                 has_insert, number_of_inserts, insert_print, insert_paper, insert_press):

        self.user = user  # trenutni korisnik
        self.product = Product.objects.get(pk=product)  # odabrani proizvod
        self.paper = Paper.objects.get(pk=paper)  # odabrani papir
        self.press = Press.objects.get(pk=press)  # odabrana vrsta tiska
        self.number_of_copies = int(number_of_copies)  # naklada - broj primjeraka
        self.product_format = Format.objects.get(pk=paper_format)  # format papira

        self.has_insert = has_insert
        self.number_of_inserts = int(number_of_inserts) if number_of_inserts else 0
        self.insert_print = insert_print
        self.insert_paper = Paper.objects.get(pk=insert_paper) if insert_paper else None
        self.insert_press = Press.objects.get(pk=insert_press) if insert_press else None

        self.printing_price = 0
        self.printing_printer = None

        self.insert_price = 0
        self.insert_printer = None

        self.product_price = 0

    def get_price(self):
        return float(self.product_price)

    def calculate_price(self):
        self.printing_price, self.printing_printer = self.get_printing_price()
        self.insert_price, self.insert_printer = self.get_insert_price()

        self.product_price = self.printing_price + self.insert_price

    def get_printing_price(self):
        """
        Funkcija nalazi cijenu naisplativijeg tiska.
        Prolazi korz printere definirane te računa cijenu za svaki od tih strojeva i vraća najnižu cijenu

        Returns:
            Funkcija vraća cijenu i printer

        """
        product_printers = self.product.printer.all()

        product_price = 0
        most_affordable_printer = None

        for printer in product_printers:
            printer_price = self.calculate_printer_printing_price(printer)

            if product_price == 0 or printer_price < product_price:
                product_price = printer_price
                most_affordable_printer = printer

        return product_price, most_affordable_printer

    def get_insert_price(self):
        """
        Funkcija nalazi cijenu  umetka.
        Cijena umetka sastoji se od dvije komponente.
            1. Cijena umetanja - računa se po formuli start + (naklada * broj_umetanja * cijena_po_umetku)
            2. Tisak umetka - traži se najisplativija opcija kao i kod tiska

        Returns:
            Funkcija vraća cijenu i stroj

        """
        insert_price = 0

        if self.has_insert:
            insert_price_object = InsertPrice.objects.filter(number_of_inserts_per_copy=self.number_of_inserts).get()
            insert_price = insert_price_object.start_price + (self.number_of_copies * self.number_of_inserts *
                                                              insert_price_object.price_per_insert)

        return insert_price, None

    def calculate_printer_printing_price(self, printer):
        """
        Cijena printa za printer.
        Funkcija prvo dohvaća cijenu papira ovisno o dimenziji, zatim računa broj proizvoda koji stane na
        stranicu stroja.
        Ovisno o tome ima li korisnik definiranu cijenu printa dohvaća se cijena az korisnika ili cijena za taj stroj

        Args:
            printer: stroj
            paper_price: cijena papira

        Returns:
            Funkcija vraća cijenu

        """
        # cijena papira ovisno o odabranom printeru
        paper_price = self.calculate_paper_price(printer.width, printer.height)

        # broj proizvoda po veličina printa za printer
        products_per_sheet = self.calculate_number_of_products_per_printer_printing_area(
            printer.width, printer.height, self.padding, self.padding)

        # broj araka - odnosno jedinica papira za taj printer
        number_of_sheets = int(math.ceil(int(self.number_of_copies) / float(products_per_sheet)))

        # slučaj ako korisnik ima definiranu cijenu klika i cijenu starta, mora i stroj biti definiran za davanje popusta
        if self.user.start_price and self.user.click_price and printer.user_discount is True:
            price = self.get_user_price(number_of_sheets, paper_price)
        else:
            price = self.get_printer_price(number_of_sheets, paper_price)

        return price

    def get_user_price(self, number_of_sheets, paper_price):
        """
        Cijena printa za korisnika.
        Cijena se računa po formuli cijena_starta + broj_klikova * (cijena_klika +  cijena_papira), u slučaju da je
        se radi o obostranom print cijene se množi s dva

        Args:
            printer: stroj
            paper_price: cijena papira

        Returns:
            Funkcija vraća cijenu

        """
        # cijena printa za korisnika je cijena starta za korisnika + broj araka*(cijena klika + cijena papira)
        if self.press.both_sides_print:
            price = self.user.start_price + number_of_sheets*(2 * self.user.click_price + paper_price)
        else:
            price = self.user.start_price + number_of_sheets*(self.user.click_price + paper_price)

        return price

    def get_printer_price(self, printer, number_of_sheets, paper_price):
        """
        Cijena printa za određeni stroj.
        Cijena se računa po formuli cijena_starta + (broj_klikova * cijena klika), u slučaju da je
        težina papira veća od feinirane granice težine dodaje se još i cijena papira

        Args:
            printer: stroj
            number_of_sheets: broj klikova
            paper_price: cijena papira

        Returns:
            Funkcija vraća cijenu

        """

        # cijena za taj printer i za broj araka
        printing_price = PrintingPrice.objects\
            .filter(printer_id=printer.id)\
            .filter(quire_from__lte=number_of_sheets)\
            .filter(quire_to__gte=number_of_sheets)\
            .get()

        number_of_prints = 1  # broj tisaka po komadu papira - obostrani tisak je 2, obični tisak je 1

        # ako je obostrani print
        if self.press.both_sides_print:
            printing_price = printing_price.filter(both_sides=True)
            number_of_prints = 2

        # start + (broj araka * cijena arka)
        price = printing_price.start_price + (number_of_prints * number_of_sheets * printing_price.click_price)

        # ako je papir teži od definirane granice težine ili ako je papir kvalitetniji dodaje se još i cijena papira
        if self.paper.paper_weight.weight > self.paper_weight_payment_threshold \
                or self.paper.paper_type.better_quality_paper is True:
            price = price + (paper_price * number_of_sheets)

        return price

    def calculate_paper_price(self, width, height):
        """
        Cijena papira po veličini papira.
        Izračunava se cijena papir aovisno o težini i veličini

        Args:
            width: širina printera
            height: visina printera

        Returns:
            Funkcija vraća broj proizvoda na formatu printera

        """
        paper_price = (Decimal(width)/1000)*(Decimal(height)/1000)*self.paper.paper_weight.weight*(self.paper.price_per_kilogram/1000)
        return paper_price

    def calculate_number_of_products_per_printer_printing_area(self, width, height, width_padding, height_padding):
        """
        Funkcija izračunava broj proizvoda po formatu printera.
        Izračunava se najveći mogući broj proizvoad po formatu kako bi iskoristivost bila što veća

        Args:
            width: širina printera
            height: visina printera
            width_padding: padding na širinu proizvoda
            height_padding: padding na visinu proizvoda

        Returns:
            Funkcija vraća broj proizvoda na formatu printera

        """
        product_width = self.product_format.width + width_padding  # širina proizvoda s napustom
        product_height = self.product_format.height + height_padding  # visina proizvoda s napustom

        products_per_horizontal_sheet = int(width/float(product_width)) * int(height/float(product_height))
        products_per_vertical_sheet = int(height/float(product_width)) * int(width/float(product_height))

        if products_per_horizontal_sheet > products_per_vertical_sheet:
            products_per_sheet = products_per_horizontal_sheet
        else:
            products_per_sheet = products_per_vertical_sheet

        return products_per_sheet