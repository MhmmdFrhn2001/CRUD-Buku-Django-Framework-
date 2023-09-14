from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('books', views.book_list, name='book_list'),
    path('books/add', views.add_book, name='add_book'),
    path('books/<int:pk>/remove_confirmation', views.remove_book_confirmation, name='remove_book_confirmation'),
    path('books/<int:pk>/remove', views.remove_book, name='remove_book'),
    path('books/<int:pk>/edit', views.edit_book, name='edit_book'),
]