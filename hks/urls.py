from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('dsgn/',views.docsign),
    path('psgn/',views.patsign),
    path('register/<slug:pid>/',views.register),
    path('login/<slug:pid>/',views.login),
    path('logout/',views.logout),
]
