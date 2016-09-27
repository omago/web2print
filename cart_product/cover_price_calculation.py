#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *
from .finish_price_calculation import FinishPriceCalculation
from product.models import ProductCoverFinish


class CoverPriceCalculation:

    def __init__(self, volume, product_format, number_of_copies, has_cover, cover_paper, cover_finishes):
        self.volume = volume
        self.product_format = product_format

        self.has_cover = has_cover
        self.number_of_copies = number_of_copies
        self.cover_paper = cover_paper
        self.cover_finishes = cover_finishes
        self.total_cover_price = 0

    def get_price(self):
        """
        Funkcija konvertira cijenu u float

        Returns:
            Funkcija vraća cijenu

        """
        return Decimal(self.total_cover_price)

    def calculate_price(self):
        """
        Funkcija kojom se poziva izračun

        Returns:
            Funkcija ne vraća ništa, dodaje cijenu svake dorade na finish_price

        """
        if self.has_cover:
            if len(self.cover_finishes):
                cover_finish_calculation = FinishPriceCalculation(finishes=self.cover_finishes,
                                                                  volume=self.volume,
                                                                  product_format=self.product_format,
                                                                  number_of_copies=self.number_of_copies,
                                                                  finish_model=ProductCoverFinish)
                cover_finish_calculation.calculate_price()
                self.total_cover_price += cover_finish_calculation.get_price()