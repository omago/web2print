#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('user.frontend_views',
    url(r'^odjava', 'logout_user', name="user-logout"),
    url(r'^moj-racun', 'my_account', name="user-my-account"),
    url(r'^registracija', 'register', name="user-register"),
    url(r'^aktivacija/(?P<pk>.*)/(?P<activation_code>.*)', 'activate', name="user-activate"),
    url(r'^reset-lozinke/(?P<pk>.*)/(?P<reset_password_code>.*)', 'reset_password', name="user-reset-password"),
    url(r'^uspjesna-registracija', 'successful_registration', name="user-successful-registration"),
    url(r'^reset-lozinke-zatrazen', 'reset_password_requested', name="user-reset-password-requested"),
    url(r'^uspjesno-promjenjena-lozinka', 'successful_password_change', name="user-successful-password-change"),
    url(r'^zaboravljena-lozinka', 'forgotten_password', name="user-forgotten-password"),
    url(r'^prijava', 'login', name="user-login"),
)