from django.contrib import admin
from django.urls import path, include

from shop.views import CategoryList

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category'),
]