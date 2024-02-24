from django.contrib import admin
from .models import Book, SoldBook
# Register your models here.
admin.site.register(Book)
admin.site.register(SoldBook)