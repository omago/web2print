#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from .models import CartProduct
from format.models import Format
from paper.models import Paper
from press.models import Press
from finish.models import Finish
from finish_type.models import FinishType
from cart_product.finish_widget import FinishWidget

from product.models import ProductFinish, ProductCoverFinish


class CartProductForm(forms.ModelForm):

    format_choices = forms.ChoiceField(label="Format (ŠxV)")
    custom_choice = [('custom', 'Custom')]

    def __init__(self, product, user, request, *args, **kwargs):
        super(CartProductForm, self).__init__(*args, **kwargs)
        self.user = user
        self.product = product
        self.product_price = 0

        self.cart_id = request.session.get("cart_id", None)

        self.fields['product'].widget = forms.HiddenInput()
        self.fields['product'].initial = self.product

        if not product.has_title:
            self.fields.pop('title')

        self.fields["format"].queryset = Format.get_product_formats(user=self.user, product=self.product)

        format_choices_list = list(self.fields['format'].choices)
        if not user.is_anonymous():
            format_choices_list += self.custom_choice

        self.fields['format_choices'].choices = format_choices_list

        self.fields["paper"].queryset = Paper.objects.filter(pk__in=self.product.paper.all())
        self.fields["press"].queryset = Press.objects.filter(pk__in=self.product.press.all())

        if not product.has_mutations:
            self.fields.pop('number_of_mutation')

        if not product.has_volume:
            self.fields.pop('volume')

        if not product.has_cover:
            self.fields.pop('has_cover')
            self.fields.pop('cover_paper')
            self.fields.pop('cover_finish')
            self.fields.pop('cover_finish_type')
        else:
            self.fields["cover_paper"].queryset = Paper.objects.filter(pk__in=self.product.cover_paper.all())
            self.fields["cover_finish"].widget.attrs.update({"product": product, "order": "cover_finish_order",
                                                             "cover": True, "model": ProductCoverFinish})

        if not product.has_insert:
            self.fields.pop('has_insert')
            self.fields.pop('number_of_inserts')
            self.fields.pop('has_insert_print')
            self.fields.pop('insert_paper')
            self.fields.pop('insert_press')
            self.fields.pop('insert_volume')
        else:
            self.fields["insert_paper"].queryset = Paper.objects.filter(pk__in=self.product.insert_paper.all())
            self.fields["insert_press"].queryset = Press.objects.filter(pk__in=self.product.insert_press.all())

        self.fields["finish"].widget.attrs.update({"product": product, "order": "finish_order",
                                                   "model": ProductFinish})

    def save(self):
        cart_product_form = super(CartProductForm, self).save(commit=False)

        # save cart and product data
        cart_product_form.cart_id = self.cart_id
        cart_product_form.product_id = self.product.pk
        cart_product_form.save()

        return cart_product_form

    class Meta:
        model = CartProduct
        exclude = ['slug', 'cart']

        widgets = {
            'finish': FinishWidget(),
            'cover_finish': FinishWidget(),
        }