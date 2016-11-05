#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *
from finish_type.models import FinishType


class WeightCalculation:
    """
    Klasa služi za izračunavanje težine proizvoda.

    Težina proizvoda sastoji se do 3 komponente:
    1. težina knjižnog bloka - get_book_block_weight
    2. težina umetka - get_insert_weight
    3. težina korica - get_cover_weight

    """

    def __init__(self, params):
        """
        :param params: parametri cijelog izračuna
        """
        self.params = params

    def calculate_product_weight(self):
        """
        Funkcija pokreće izračun težine
        """
        self.get_book_block_weight()
        self.get_insert_weight()
        self.get_cover_weight()

        self.params.product_weight = self.params.book_block_weight + self.params.insert_weigh + self.params.cover_weight

    def get_book_block_weight(self):
        """
        Funkcija računa težinu knjižnog bloka.

        Težina knjižnog bloga računa se po formuli:
        (širina * visina * opseg * broj mutacija * broj stranica * broj kopija * težina papira)

        """
        total_surface = self.params.product_format.width * self.params.product_format.height * \
            self.params.volume * self.params.number_of_copies * self.params.number_of_mutation

        self.params.book_block_weight = total_surface * self.params.paper.paper_weight.weight

    def get_insert_weight(self):
        """
        Funkcija računa težinu umetka.

        Težina umetka računa se po formuli:
        (širina * visina * opseg umetka * broj umetanja * broj kopija * težina papira)

        """
        if self.params.has_insert:
            total_surface = self.params.product_format.width * self.params.product_format.height * \
                self.params.number_of_inserts * self.params.insert_volume * self.params.number_of_copies

            self.params.insert_weigh = total_surface * self.params.insert_paper.paper_weight.weight

    def get_cover_weight(self):
        """
        Funkcija računa težinu korica.

        Težina korica računa se po formuli:
        (širina * visina * opseg umetka * 2 * broj kopija * težina papira)

        """
        #TODO: još jednom proći kako hrbat utječe na ovu težinu, posotji model Spine koji definira debljinu hrbta za određene dorade
        if self.params.has_cover:
            spine_surface = self.params.volume * self.params.paper.paper_thickness * self.params.product_format.width

            total_surface = self.params.product_format.width * self.params.product_format.height * 2 * \
                self.params.number_of_copies * spine_surface

            finish_weight = Decimal(0)

            for finish in self.params.cover_finishes:
                if "finish_type_id" in finish and finish["finish_type_id"]:
                    finish_type = FinishType.get(finish["finish_type_id"])
                    finish_weight += total_surface * finish_type.weight

            self.params.cover_weight = (total_surface * self.params.cover_paper.paper_weight.weight) + finish_weight
