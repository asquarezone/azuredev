import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
]
