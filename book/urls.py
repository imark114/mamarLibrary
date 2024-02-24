from django.urls import path
from . import views
urlpatterns = [
    path('book_details/<int:id>/', views.BookDetailView.as_view(), name='book_details'),
    path('buy_book/<int:id>/', views.BuyBook, name='buy_book'),
    path('return_book/<int:id>/', views.ReturnBook, name='return_book')
]
