from django.contrib import admin
from django.urls import path, include

from OnlineLibrary.account import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('delete/', views.profile_delete, name='profile_delete'),
]