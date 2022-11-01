from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
# from django import forms

import mysite.models as models

class SiteLoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(SiteLoginForm, self). __init__(request=request, *args, **kwargs)

    def clean(self):
        super(SiteLoginForm, self).clean()
