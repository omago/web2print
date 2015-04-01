#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from decimal import *

from django.db.models import Q
from django import forms

from .models import CartProduct
from format.models import Format
from paper.models import Paper
from press.models import Press
from plastic.models import Plastic
from binding.models import Binding
from flexion.models import Flexion
from printing_price.models import PrintingPrice
from cart.models import Cart


class CartProductForm(forms.ModelForm):

    user_format_width = forms.IntegerField(label="Širina", required=False)
    user_format_height = forms.IntegerField(label="Visina", required=False)
    user_format_add_to_user_formats = forms.BooleanField(label="Dodaj u moje formate", required=False)

    def __init__(self, product, user, request, *args, **kwargs):
        super(CartProductForm, self).__init__(*args, **kwargs)
        self.user = user
        self.product = product
        self.product_price = 0

        self.cart_id = request.session.get("cart_id", None)

        if not self.cart_id:
            cart = Cart()
            cart.user = self.user
            cart.save()

            self.cart_id = cart.pk
            request.session["cart_id"] = self.cart_id

        self.fields.keyOrder = []

        self.fields['product'].widget = forms.HiddenInput()
        self.fields['product'].initial = self.product

        if not product.has_title:
            self.fields.pop('title')
        else:
            self.fields.keyOrder.append('title')

        self.fields.keyOrder.append('format')
        self.fields["format"].queryset = Format.objects.filter(Q(pk__in=self.product.formats.all()) | Q(user=self.user, product_subcategory=self.product.subcategory))
        self.fields.keyOrder.append('user_format_width')
        self.fields.keyOrder.append('user_format_height')
        self.fields.keyOrder.append('user_format_add_to_user_formats')
        self.fields.keyOrder.append('paper')
        self.fields["paper"].queryset = Paper.objects.filter(pk__in=self.product.paper.all())
        self.fields.keyOrder.append('press')
        self.fields["press"].queryset = Press.objects.filter(pk__in=self.product.press.all())
        self.fields.keyOrder.append('number_of_copies')

        if not product.has_mutations:
            self.fields.pop('number_of_mutation')
        else:
            self.fields.keyOrder.append('number_of_mutation')

        if not product.has_cover:
            self.fields.pop('cover_paper')
            self.fields.pop('cover_plastic')
        else:
            self.fields.keyOrder.append('cover_paper')
            self.fields["cover_paper"].queryset = Paper.objects.filter(pk__in=self.product.cover_paper.all())
            self.fields.keyOrder.append('cover_plastic')
            self.fields["cover_plastic"].queryset = Plastic.objects.filter(pk__in=self.product.cover_plastic.all())

        if not product.has_insert:
            self.fields.pop('insert_paper')
        else:
            self.fields.keyOrder.append('insert_paper')
            self.fields["insert_paper"].queryset = Paper.objects.filter(pk__in=self.product.insert_paper.all())

        #
        # DORADE
        #
        if not product.has_cutting:
            self.fields.pop('cutting')
        else:
            self.fields.keyOrder.append('cutting')

        if not product.has_improper_cutting:
            self.fields.pop('improper_cutting')
        else:
            self.fields.keyOrder.append('improper_cutting')

        if not product.has_creasing:
            self.fields.pop('creasing')
        else:
            self.fields.keyOrder.append('creasing')

        if not product.has_hole_drilling:
            self.fields.pop('hole_drilling')
        else:
            self.fields.keyOrder.append('hole_drilling')

        if not product.has_vacuuming:
            self.fields.pop('vacuuming')
        else:
            self.fields.keyOrder.append('vacuuming')

        if not product.has_binding:
            self.fields.pop('bindings')
        else:
            self.fields.keyOrder.append('bindings')
            self.fields["bindings"].queryset = Binding.objects.filter(pk__in=self.product.bindings.all())

        if not product.has_flexion:
            self.fields.pop('flexion')
        else:
            self.fields.keyOrder.append('flexion')
            self.fields["flexion"].queryset = Flexion.objects.filter(pk__in=self.product.flexion.all())

        if not product.has_laminating:
            self.fields.pop('laminating')
        else:
            self.fields.keyOrder.append('laminating')

        if not product.has_plastic:
            self.fields.pop('plastic')
        else:
            self.fields.keyOrder.append('plastic')
            self.fields["plastic"].queryset = Plastic.objects.filter(pk__in=self.product.plastic.all())

        if not product.has_rounding:
            self.fields.pop('rounding')
        else:
            self.fields.keyOrder.append('rounding')

    # popraviti metodu
    def clean(self):
        cleaned_data = super(CartProductForm, self).clean()

        user_format_width = cleaned_data['user_format_width']
        user_format_height = cleaned_data['user_format_height']

        if user_format_width and user_format_height:
            pass
            #del self.errors['format']

        return cleaned_data

    def save(self):
        cart_product_form = super(CartProductForm, self).save(commit=False)

        user_format_add_to_user_formats = self.cleaned_data['user_format_add_to_user_formats']
        user_format_width = self.cleaned_data['user_format_width']
        user_format_height = self.cleaned_data['user_format_height']

        if user_format_width and user_format_height:
            user_format = Format()
            user_format.width = user_format_width
            user_format.height = user_format_height
            user_format.user = self.user
            user_format.product_subcategory = self.product.subcategory
            if user_format_add_to_user_formats:
                user_format.user_format = True
            user_format.save()

            cart_product_form.user_format = user_format

        # save cart and product data
        cart_product_form.cart_id = self.cart_id
        cart_product_form.product_id = self.product.pk
        cart_product_form.save()

        return cart_product_form

    class Meta:
        model = CartProduct
        exclude = ['slug', 'cart']

    def calculate_price(self):
        products_per_sheet = self.calculate_products_per_sheet()
        paper = Paper.objects.get(pk=self.data["paper"])
        press = Press.objects.get(pk=self.data["press"])
        number_of_sheets = int(math.ceil(int(self.data["number_of_copies"]) / float(products_per_sheet)))
        printing_price = PrintingPrice.objects\
            .filter(printer_id=1)\
            .filter(quire_from__lte=number_of_sheets)\
            .filter(quire_to__gte=number_of_sheets)\
            .get()

        paper_price = self.calculate_paper_price(paper)

        # slučaj ako korisnik ima definiranu cijenu klika i cijenu starta
        if self.user.start_price and self.user.click_price:
            # obostrani print
            if press.both_sides_print:
                price = self.user.start_price + number_of_sheets*(2*self.user.click_price+paper_price)
            else:
                price = self.user.start_price + number_of_sheets*(self.user.click_price+paper_price)
        else:
            price = (number_of_sheets * printing_price.click_price) + printing_price.start_price
            paper_weight = paper.paper_weight.weight

            if press.both_sides_print:
                price = price*printing_price.both_sides_price

            if paper_weight > 250:
                price = price + (paper_price * number_of_sheets)

        self.product_price = format(price, '.2f')

    def calculate_paper_price(self, paper):
        paper_price = Decimal(0.33)*Decimal(0.48)*paper.paper_weight.weight*(paper.price_per_kilogram/1000)
        return paper_price

    def calculate_products_per_sheet(self):
        product_format = Format.objects.get(pk=self.data["format"])
        product_width = product_format.width + 2
        product_height = product_format.height + 2

        products_per_horizontal_sheet = int(470/float(product_width)) * int(320/float(product_height))
        products_per_vertical_sheet = int(320/float(product_width)) * int(470/float(product_height))

        if products_per_horizontal_sheet > products_per_vertical_sheet:
            products_per_sheet = products_per_horizontal_sheet
        else:
            products_per_sheet = products_per_vertical_sheet

        return products_per_sheet




