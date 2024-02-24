from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView
from .models import Book,SoldBook
from .forms import CommentForm
from django.contrib import messages
# Create your views here.
class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = 'id'
    template_name = 'book_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        book = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        comments = book.comments.all()
        context['comments'] = comments
        comment_form = CommentForm
        context['comment_form'] = comment_form
        return context

def BuyBook(request, id):
    book = Book.objects.get(pk=id)
    user = request.user
    if user.balance >= book.price:
        newSold = SoldBook()
        newSold.buyer = user
        newSold.book = book
        newSold.can_reveiw = True
        user.balance-=book.price
        user.save()
        newSold.balance_after_buy = user.balance
        newSold.save()
        return redirect('home')
    else:
        messages.warning(request,"You've no sufficient Balance to Buy the book")
        return redirect('deposit')

def ReturnBook(request, id):
    sold = SoldBook.objects.get(pk=id)
    request.user.balance+=sold.book.price
    request.user.save()
    sold.delete()
    return redirect('profile')