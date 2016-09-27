#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from decimal import *
from printing_price.models import PrintingPrice
from printer.models import Printer


class PrinterPriceCalculation():

    padding = 4  # napust kod printa
    paper_weight_payment_threshold = 250  # težina papira nakon koje se plaća i papir

    def __init__(self, printer, product_format, press, paper, number_of_copies,
                 number_of_mutations=None, volume=None, user=None, finish_affects_assembly_in_press=None):

        self.printer = printer
        self.press = press
        self.paper = paper
        self.user = user
        self.product_format = product_format
        self.product_width = self.product_format.width
        self.product_height = self.product_format.height
        self.finish_affects_assembly_in_press = finish_affects_assembly_in_press

        self.number_of_copies = number_of_copies  # naklada - broj primjeraka
        self.number_of_mutations = number_of_mutations  # broj mutacija
        self.volume = volume  # broj stranica
        self.number_of_pages_total = self.number_of_copies * self.number_of_mutations * self.volume

        # dimenzije arka
        self.sheet_width = self.printer.max_paper_width
        self.sheet_height = self.printer.max_paper_width
        self.printer_width = self.printer.printing_area_width
        self.printer_height = self.printer.printing_area_height

        self.total_price = 0
        self.products_per_sheet = None
        self.number_of_sheets = None
        self.paper_price_per_sheet = None

    def get_price(self):
        """
        Funkcija konvertira cijenu u float

        Returns:
            Funkcija vraća cijenu

        """
        return Decimal(self.total_price)

    def calculate_price(self):
        """
        Funkcija kojom se poziva izračun

        Returns:
            Funkcija vraća cijenu tiska

        """
        if self.can_product_be_printed_on_printer():
            # broj proizvoda po veličina printa za printer
            self.products_per_sheet = self.calculate_number_of_products_per_printer_printing_area(self.padding, self.padding)
            self.paper_price_per_sheet = self.calculate_paper_price()

            self.number_of_sheets = math.ceil(int(self.number_of_pages_total) / float(self.products_per_sheet))

            # slučaj ako korisnik ima definiranu cijenu klika i cijenu starta, mora i stroj biti definiran za davanje popusta
            if self.user.start_price and self.user.click_price and self.printer.user_discount is True:
                self.total_price = self.get_user_price()
            else:
                self.total_price = self.get_printer_price()

        return self.get_price()

    def calculate_paper_price(self):
        """
        Cijena papira za veličinu arka.
        Izračunava se cijena papira ovisno o težini i veličini

        Returns:
            Funkcija vraća cijenu papira po veličini arka

        """
        price_per_kilogram = self.get_paper_price_per_kilogram()
        sheet_width_in_meters = Decimal(self.sheet_width)/1000
        sheet_height_in_meters = Decimal(self.sheet_height)/1000
        paper_price = price_per_kilogram/1000

        paper_price *= sheet_width_in_meters * sheet_height_in_meters * self.paper.paper_weight.weight

        return paper_price

    def get_paper_price_per_kilogram(self):
        """
        Cijena papira po kilogramu.
        U bazi postoje dva podataka za cijenu kilograma, jedan je za rolu drugi je za običan papir. Funkcija ovisno
        o stroju vraća cijenu papira po kilogramu

        Args:
            self: instanca klase

        Returns:
            Funkcija vraća cijenu papira po veličini arka

        """
        price_per_kilogram = self.paper.price_per_kilogram

        # cijena kilograma papira za rolu.
        if self.printer.role:
            price_per_kilogram = self.paper.price_per_kilogram_role

        return price_per_kilogram

    def calculate_number_of_products_per_printer_printing_area(self, width_padding, height_padding):
        """
        Funkcija izračunava broj proizvoda po arku.
        Izračunava se najveći mogući broj proizvoad po formatu kako bi iskoristivost bila što veća

        Args:
            width_padding: padding na širinu proizvoda
            height_padding: padding na visinu proizvoda

        Returns:
            Funkcija vraća broj proizvoda na formatu printera te postavlja visinu arka u slučaju kada se tiska na rolu

        """
        product_width = self.product_width

        if self.finish_affects_assembly_in_press:
            product_width *= 2

        product_width += width_padding  # širina proizvoda s napustom
        product_height = self.product_height + height_padding  # visina proizvoda s napustom

        if self.printer.role:
            products_per_horizontal_sheet = int(self.printer_width/float(product_width))
            products_per_vertical_sheet = int(self.printer_width/float(product_height))

            if products_per_horizontal_sheet > products_per_vertical_sheet:
                products_per_sheet = products_per_horizontal_sheet
                self.sheet_height = product_height + 6
            else:
                products_per_sheet = products_per_vertical_sheet
                self.sheet_height = product_width + 6
        else:
            products_per_horizontal_sheet = int(self.printer_width/float(product_width)) * int(self.printer_height/float(product_height))
            products_per_vertical_sheet = int(self.printer_height/float(product_width)) * int(self.printer_width/float(product_height))

            if products_per_horizontal_sheet > products_per_vertical_sheet:
                products_per_sheet = products_per_horizontal_sheet
            else:
                products_per_sheet = products_per_vertical_sheet

        # u slučaju da dorada utječe na cijenu mogući su slijedeći slučajevi brojeva proizvoda po arku
        # obzirom da se u pravom koraju širina proizvoda množila s dva ovdje se broj proizvoda isto mora množiti s dva
        if self.finish_affects_assembly_in_press:
            if products_per_sheet >= 32:
                products_per_sheet = 64
            elif products_per_sheet >= 16:
                products_per_sheet = 32
            elif products_per_sheet >= 8:
                products_per_sheet = 16
            elif products_per_sheet >= 4:
                products_per_sheet = 8
            elif products_per_sheet >= 2:
                products_per_sheet = 4
            elif products_per_sheet >= 1:
                products_per_sheet = 2

        return products_per_sheet

    def can_product_be_printed_on_printer(self):
        """
        Funkcija provjerava može li se proizvod tiskati na odabranom printeru.
        Kriteriji su:
        1. Veličina formata ulazi je unutar granica veličine printera
        2. printer može printati odabrani tisak

        Args:
            self: instanca klase

        Returns:
            Funkcija vraća bool

        """
        product_can_be_printed = False

        product_width = self.product_width
        product_height = self.product_width

        # ovo je slučaj kada je uključeno da dorada utječe na cijenu tiska. Potrebno je provjeriti dali dupla
        # stranica može stati na format printera.
        if self.finish_affects_assembly_in_press:
            product_width *= 2

        if ((product_width <= self.printer_width and product_height <= self.printer_height) or
                (product_width <= self.printer_height and product_height <= self.printer_width)) and \
                (self.press in self.printer.press.all()):
            product_can_be_printed = True

        return product_can_be_printed

    def get_user_price(self):
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
        paper_price = self.number_of_sheets * self.paper_price_per_sheet

        # cijena printa za korisnika je cijena starta za korisnika + broj araka*(cijena klika + cijena papira)
        if self.press.both_sides_print:
            price = self.user.start_price + self.number_of_sheets*(2 * self.user.click_price + paper_price)
        else:
            price = self.user.start_price + self.number_of_sheets*(self.user.click_price + paper_price)

        return price

    def get_printer_price(self):
        """
        Cijena printa za određeni stroj.
        Cijena se sastoji od 3 komponente:

        1. Cijena starta
        2. Varijabilni dio cijene koji ovisi o tipu izračuna
        3. cijena papira

        Returns:
            Funkcija vraća cijenu

        """
        x_price, start_price, start_price_per_sheet = self.get_x_and_start_price()

        if self.printer.printing_price_type == Printer.COPIES:
            variable_price = (self.number_of_sheets * self.sheet_height) / self.printer.click_width * x_price
        elif self.printer.printing_price_type == Printer.M2:
            variable_price = (self.product_width/1000) * (self.product_height/1000) * x_price * self.number_of_pages_total
        elif self.printer.printing_price_type == Printer.OFFSET:  # izračun za offset, potrebno je naći koliko ploča se priprema za tisak jednog proizvoda
            number_of_sheets_per_product = int(self.volume / self.products_per_sheet)
            variable_price = (number_of_sheets_per_product * start_price_per_sheet) + self.number_of_sheets * x_price
        else:
            variable_price = self.number_of_sheets * x_price

        return start_price + variable_price + self.get_paper_price()

    def get_x_and_start_price(self):
        """
        Funkcija dohvaća cijenu x-a i cijenu starta. Funkcija rješava dva moguća slučaja

        1. Vrijednost za x je nađena u bazi, cijena x-a i cijena starta dodijeljuju se iz baze
        2. Vrijednost za x nije nađena u bazi te se računa na osnovu dva najbliža x-a.
            Dohvaća se prvi najmanji x i prvi najveći x te se cijena računa po formuli:
            acijena - ((acijena-bcijena) / (bx-ax)) * (x-ax) 

        Returns:
            Funkcija vraća cijenu x i cijenu starta

        """
        # odredi radi li se o obstranom printu
        both_sides_print = False
        if self.press.both_sides_print:
            both_sides_print = True

        # cijena se prvo dohvaća za fiksni x
        printing_price = PrintingPrice.get_x_price(self.printer, both_sides_print, self.number_of_sheets)

        # ako je x nađen u bazi dodjeljuje se cijena iz baze
        if printing_price:
            x_price = printing_price.x_price
            start_price = printing_price.start_price
            start_price_per_sheet = printing_price.start_price_per_sheet
        # ako x nije nađen u bazi onda se cijena x računa
        else:
            a = PrintingPrice.get_x_lt_price(self.printer, both_sides_print, self.number_of_sheets)
            b = PrintingPrice.get_x_gt_price(self.printer, both_sides_print, self.number_of_sheets)

            if a and b:
                x_price = a.x_price - ((a.x_price - b.x_price) / (b.x - a.x)) * (self.number_of_sheets - a.x)
                start_price = a.start_price
                start_price_per_sheet = a.start_price_per_sheet
            else:
                return float(0), float(0), float(0)

        return x_price, start_price, start_price_per_sheet

    def get_paper_price(self):
        """
        Cijena papira za nakladu.
        Cijena papira se računa u 3 slučaja

        1. Ako na stroju nije definirana granica težine
        2. Ako je papir teži od definirane granice težine
        2. Ako je tiska na kvalitetniji papir

        Returns:
            Funkcija vraća cijenu

        """
        paper_price = 0

        condition_1 = self.printer.paper_weight_payment_threshold is None or 0
        condition_2 = 0 < self.printer.paper_weight_payment_threshold < self.paper.paper_weight.weight
        condition_3 = self.paper.paper_type.better_quality_paper is True

        if condition_1 or condition_2 or condition_3:
            paper_price = self.paper_price_per_sheet * self.number_of_sheets

        return paper_price
