
from ast import Delete
import contextvars
from distutils.log import debug
import json

import uuid
import logging

from datetime import timedelta, datetime

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse_lazy
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_safe
from django.views.generic import DetailView, TemplateView, View, CreateView, UpdateView, FormView
# from django.utils import timezone, dateformat
from django.shortcuts import render, get_object_or_404

# from django_tables2 import RequestConfig

from django.core.exceptions import PermissionDenied
# from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import (
        LoginView,
        LogoutView,
        PasswordChangeView,
        PasswordChangeDoneView,
    )
from mysite import forms
from mysite import models

from django.db.models import Sum, Avg

from pprint import pprint


# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from mysite.serializers import BookingSerializer

logger = logging.getLogger(__name__)


def format_date(value):
    if value is not None:
        return value.strftime(settings.DATE_FORMAT_UI)
    else:
        return ''


class SiteLogin(LoginView):
    form_class = forms.SiteLoginForm
    template_name = 'mysite/login.html'
    print("SiteLogin")

    def get_context_data(self, **kwargs):
        context = super(SiteLogin, self).get_context_data(**kwargs)
        return context


class SiteLogoutView(LogoutView):
    template_name = 'mysite/logout.html'

    def dispatch(self, request, *args, **kwargs):
        login_url = reverse_lazy('login')
        return HttpResponseRedirect(login_url)


class SitePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'mysite/password_change.html'
    success_url = reverse_lazy('password-change-done')


class SitePasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'mysite/password_change_done.html'


class AccessDenied(LoginRequiredMixin, TemplateView):
    template_name = 'mysite/access_denied.html'
    login_url = reverse_lazy('login')


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'mysite/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        profile = models.Profile.objects.get(user=self.request.user)
        context['profile'] = profile
        return context
        
