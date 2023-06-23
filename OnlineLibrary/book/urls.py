from django.urls import path, include

from OnlineLibrary.book import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:id>/', views.edit_book, name='edit_book'),
    path('details/<int:id>/', views.details_book, name='details_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
]