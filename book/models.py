from django.db import models
# from django.contrib.auth.models import User
from category.models import Category
from account.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title

class SoldBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='buy_book')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    timestmp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    balance_after_buy = models.DecimalField(decimal_places=2,max_digits=12, null=True, blank=True)
    can_reveiw = models.BooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return f"{self.book.title} - {self.buyer.first_name}"

class Comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    