#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True, db_index=True, verbose_name="Korisničko ime")
    company = models.CharField(max_length=254, null=True, blank=True, verbose_name="Tvrtka")
    oib = models.CharField(max_length=254, verbose_name="OIB")
    address = models.CharField(max_length=254, null=True, verbose_name="Adresa")
    activation_code = models.CharField(max_length=254, null=True, blank=True)
    reset_password_code = models.CharField(max_length=254, null=True, blank=True)
    reset_password_code_expiration = models.DateTimeField(null=True, blank=True)
    e_mail = models.EmailField(max_length=254, unique=True, verbose_name="E-mail")
    phone = models.CharField(max_length=254, null=True, blank=True, verbose_name="Telefon/mobitel")
    contact_person = models.CharField(max_length=254, null=True, blank=True, verbose_name="Osoba za kontakt")
    start_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True, verbose_name="Cijena starta")
    click_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True, verbose_name="Cijena klika")
    discount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True, verbose_name="Popust")
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['twitter_handle']

    class Meta:
        ordering = ['-pk']
        db_table = "user"

    def get_username(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True