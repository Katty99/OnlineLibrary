from django.urls import path, include

from OnlineLibrary.common import views

urlpatterns = [
    path('', views.home, name='home')
]