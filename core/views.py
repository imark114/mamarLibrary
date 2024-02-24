from django.shortcuts import render
from category.models import Category
from book.models import Book
# Create your views here.

def home(request, category_slug = None):
    books = Book.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        books = Book.objects.filter(category= category)
    categories = Category.objects.all()
    return render(request,'index.html',{'categories': categories, 'books': books})