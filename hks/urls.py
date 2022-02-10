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
    path('create_blog/',views.create_blog),
    path('my_blog/',views.my_blog),
    path('see_blog/<slug:pid>/',views.see_blog),
    path('booking_form/<slug:pid>/',views.booking_form),
    path('Book_appointment/<slug:pid>/',views.Book_appointment)
]
