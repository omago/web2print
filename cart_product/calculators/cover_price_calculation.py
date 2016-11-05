#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *
from .finish_price_calculation import FinishPriceCalculation
from product.models import ProductCoverFinish


class CoverPriceCalculation:

    def __init__(self, params, cover_finishes):
        self.params = params
        self.cover_finishes = cover_finishes
        self.total_cover_price = 0

    def calculate_price(self):
        """
        Funkcija kojom se poziva izračun

        Returns:
            Funkcija ne vraća ništa, dodaje cijenu svake dorade na finish_price

        """
        if self.params.has_cover and len(self.cover_finishes):
            cover_finish_calculation = FinishPriceCalculation(self.params, self.cover_finishes, ProductCoverFinish)
            self.total_cover_price += cover_finish_calculation.calculate_price()

        #TODO: Korice imaju papir, kako to utječe na cijenu?
        #TODO: Dali je jedini trošak korice samo dorada?

        return Decimal(self.total_cover_price)
