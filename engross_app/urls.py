from django.contrib import admin
from django.urls import path,include
from .views import home, form

urlpatterns = [
    path('', home, name="home"),
    path('form', form, name="form"),


]