from django.contrib import admin
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.get_notes, name="home")
]
