from django.urls import path
from . import views

app_name = 'demo'
urlpatterns = [
    path('index', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('addBook/', views.add_book, name='addBook'),
    path('delBook/<int:book_id>', views.delete_book, name='delBook'),
    path('editBook/<int:book_id>', views.edit_book, name='editBook'),
]