#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import md5
import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms.util import ErrorList

from .models import User


class UserAccountForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=True, label="Potvrda lozinke")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Lozinka")

    def __init__(self, *args, **kwargs):
        super(UserAccountForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data
        if self.instance and self.instance.pk is not None:
            if not cleaned_data.has_key("password") and not cleaned_data.has_key("password_confirm"):
                del self.errors['password']
                del self.errors['password_confirm']

        if cleaned_data.has_key("password") and cleaned_data.has_key("password_confirm"):
            password = cleaned_data['password']
            password_confirm = cleaned_data['password_confirm']
            if password_confirm != password:
                self.errors["password_confirm"] = ErrorList()
                self.errors["password_confirm"].append("Lozinke se ne poklapaju, molimo upišite ponovno.")

        return cleaned_data

    class Meta:
        model = User
        verbose_name = "Korisnik"
        verbose_name_plural = "Korisnici"
        exclude = ('last_login', 'date_joined', 'activation_code', 'is_active', 'is_superuser', 'reset_password_code', 'reset_password_code_expiration')

    def save(self, commit=True):
        user = super(UserAccountForm, self).save(commit=False)
        if user.pk:
            if self.cleaned_data.has_key("password"):
                user.set_password(self.cleaned_data["password"])
            else:
                existing_user = User.objects.get(pk=user.pk)
                user.password = existing_user.password
        else:
            user.set_password(self.cleaned_data["password"])
            user.activation_code = md5(str(datetime.datetime.now()) + self.cleaned_data["username"]).hexdigest()

        if commit:
            user.save()

        return user

class UserLoginForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput(attrs={"placeholder": "Korisničko ime"}), label="Korisničko ime")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Lozinka"}), label="Lozinka")
    remember_me = forms.CharField(widget=forms.CheckboxInput(), initial=True, required=False, label="Zapamti me")

class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Lozinka"}), label="Lozinka")
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Potvrda lozinke"}), label="Potvrda lozinke")

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.has_key("password") and cleaned_data.has_key("password_confirm"):
            password = cleaned_data['password']
            password_confirm = cleaned_data['password_confirm']
            if password_confirm != password:
                self.errors["password_confirm"] = ErrorList()
                self.errors["password_confirm"].append("Lozinke se ne poklapaju, molimo upišite ponovno.")

        return  cleaned_data

class ForgottenPasswordForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput(attrs={"placeholder": "Korisničko ime"}), label="Korisničko ime")

    def clean(self):
        if self.cleaned_data.has_key("username"):
            username = self.cleaned_data["username"]

            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                self.errors["username"] = ErrorList()
                self.errors["username"].append("Korisnik nije nađen u našoj bazi.")

        return self.cleaned_data