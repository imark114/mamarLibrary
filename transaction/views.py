from django.shortcuts import render, redirect
from .forms import Transaction
from .forms import TransactionForm
from django.urls import reverse_lazy
# Create your views here.

def deposit_view(request):
    form = TransactionForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            deposit_amount = form.cleaned_data['amount']
            deposit = Transaction.objects.create(
                account=request.user,
                amount= deposit_amount
            )
            deposit.save()
            request.user.balance+=deposit_amount
            request.user.save()
            return redirect('home')
    return render(request, 'account/form.html',{'form': form, 'type': 'Deposit'})