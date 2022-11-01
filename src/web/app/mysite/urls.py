from django.contrib import admin
from django.urls import path

from mysite import views


urlpatterns = [
     path("",
          views.HomeView.as_view(),
          ),
     path("home/",
          views.HomeView.as_view(),
          name='home'),
     

     path('login/',
          views.SiteLogin.as_view(),
          name='login'),
     path('logout/',
          views.SiteLogoutView.as_view(),
          name='logout'),
     path('password_change/',
          views.SitePasswordChangeView.as_view(),
          name='password-change'),
     path('password_change_done/',
          views.SitePasswordChangeDoneView.as_view(),
          name='password-change-done'),
     path('access_denied/',
          views.AccessDenied.as_view(),
          name='access-denied'),

]
