from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rezet_app import views

urlpatterns = [
	path("", views.home),
	path("login/",views.login),
	path("signup/",views.signup),



	]