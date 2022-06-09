from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_product, name='register_product'),
    path('find/<str:name>', views.find_product, name='product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
    path('update/<int:id>', views.edit, name='update'),
    path('update/update_product/<int:id>', views.update_product, name='update_product')
]
