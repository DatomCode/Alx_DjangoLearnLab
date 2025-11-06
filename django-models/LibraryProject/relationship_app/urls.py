from django.urls import path
from .import views

urlpatterns = [
    path('', views.lists_all_books),
    path('books/', views.LibraryView),
]
