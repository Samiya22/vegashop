from email import header
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('header/', body),

]