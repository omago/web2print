#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import md5
import datetime
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout

from e_mail.e_mail import Email
from .forms import UserAccuntForm, UserLoginForm, ForgottenPasswordForm, ResetPasswordForm
from .models import User

def register(request):

    if request.POST:
        form = UserAccuntForm(request.POST)

        if form.is_valid():
            user = form.save()
            form.save_m2m()

            activation_link = "http://" + request.META['HTTP_HOST'] + reverse("user-activate",
                                                                              kwargs={'pk': user.pk,
                                                                                      "activation_code": user.activation_code})

            email = Email()
            email.add_recipient(user.e_mail)
            email.subject = "Aktivacija računa u Web2print trgovini"
            email.content = "<h1>" + email.subject + "</h1>" \
                           "<p>Molimo da aktivirate svoj račun <a href='" + activation_link + "'>ovdje</a>." \
                           "</p>"

            email.send()

            return HttpResponseRedirect(reverse("user-successful-registration"))
    else:
        form = UserAccuntForm()

    context = {}

    context.update(csrf(request))
    context['form'] = form
    context['page_title'] = "Registracija"

    return render_to_response('frontend/user_account/register.html', context, context_instance=RequestContext(request))

def forgotten_password(request):

    if request.POST:
        form = ForgottenPasswordForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            user = User.objects.get(username=username)
            user.reset_password_code = md5(str(datetime.datetime.now()) + username).hexdigest()
            user.reset_password_code_expiration = timezone.now() + datetime.timedelta(minutes=15)
            user.save()

            activation_link = "http://" + request.META['HTTP_HOST'] + reverse("user-reset-password",
                                                                              kwargs={'pk': user.pk,
                                                                                      "reset_password_code": user.reset_password_code})

            email = Email()
            email.add_recipient(user.e_mail)
            email.subject = "Resetiranje pristupne lozinke u Web2print trgovini"
            email.content = "<h1>" + email.subject + "</h1>" \
                           "<p>Resetirati svoju lozinku možete <a href='" + activation_link + "'>ovdje</a>." \
                           "</p>"

            email.send()

            return HttpResponseRedirect(reverse("user-reset-password-requested"))
    else:
        form = ForgottenPasswordForm()

    context = {}

    context.update(csrf(request))
    context['form'] = form
    context['page_title'] = "Zaboravljena lozinka"

    return render_to_response('frontend/user_account/forgotten_password.html', context, context_instance=RequestContext(request))

@login_required
def my_account(request):
    user = request.user
    updated = False
    if request.POST:
        form = UserAccuntForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            form.save_m2m()
            updated = True
    else:
        form = UserAccuntForm(instance=user)

    context = {}

    context.update(csrf(request))
    context['form'] = form
    context['updated'] = updated
    context['page_title'] = "Moj račun"

    return render_to_response('frontend/user_account/my_account.html', context, context_instance=RequestContext(request))

def activate(request, pk, activation_code):
    error = False

    try:
        user = User.objects.get(pk=pk)
        if user.activation_code == activation_code and user.is_active == False:
            user.is_active = True
            user.save()
        else:
            error = True
    except User.DoesNotExist:
        error = True

    context = {"error": error,
               "page_title": "Aktivacija"}

    return render_to_response('frontend/user_account/activate.html', context, context_instance=RequestContext(request))

def login(request):
    error = None

    if request.POST:
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                if not request.POST.get('remember_me'):
                    request.session.set_expiry(0)
                return HttpResponseRedirect(reverse("index-page"))
            else:
                error = True
        else:
            error = True
    else:
        form = UserLoginForm()

    context = {}

    context.update(csrf(request))
    context['form'] = form
    context['error'] = error
    context['page_title'] = "Prijava"

    return render_to_response('frontend/user_account/login.html', context, context_instance=RequestContext(request))

def reset_password(request, pk, reset_password_code):
    error = None

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        error = True

    if not error:
        context = {}
        context.update(csrf(request))

        validation_error = False
        form = ResetPasswordForm()

        if user.reset_password_code != reset_password_code or user.reset_password_code_expiration < timezone.now():
            validation_error = True
        else:
            if request.POST:
                form = ResetPasswordForm(request.POST)

                if form.is_valid():
                    password = form.cleaned_data["password"]
                    user.set_password(password)
                    user.save()

                    return HttpResponseRedirect(reverse("user-successful-password-change"))

        context['form'] = form
        context['pk'] = pk
        context['reset_password_code'] = reset_password_code
        context['error'] = error
        context['validation_error'] = validation_error
        context['page_title'] = "Reset lozinke"

        return render_to_response('frontend/user_account/reset_password.html', context, context_instance=RequestContext(request))
    else:
        return HttpResponse()

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("index-page"))

def reset_password_requested(request):
    return render_to_response('frontend/user_account/reset_password_requested.html', context_instance=RequestContext(request))

def successful_password_change(request):
    return render_to_response('frontend/user_account/successful_password_change.html', context_instance=RequestContext(request))

def successful_registration(request):
    return render_to_response('frontend/user_account/successful_registration.html', context_instance=RequestContext(request))

