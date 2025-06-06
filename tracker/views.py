from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CurrentBalance, TrackingHistory


# Create your views here.
def index(request):
    if request.method == 'POST':
        current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)

        description = request.POST.get('description')
        amount = request.POST.get('amount')

        expense_type = 'CREDIT'
        if float(amount) < 0:
            expense_type = 'DEBIT'

        if float(amount) == 0:
            messages.warning(request,'Amount Cannot be Zero')
            return redirect('/')


        tracking_history = TrackingHistory.objects.create(
            current_balance = current_balance,
            amount = amount,
            expense_type = expense_type,
            description = description
        )

        current_balance.current_balance += float(tracking_history.amount)
        current_balance.save()

        return redirect('/')   
    # current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
    tracking_history = TrackingHistory.objects.all()
    credit_amount = 0
    debit_amount = 0
    for transaction in tracking_history:
        if transaction.expense_type == 'CREDIT':
            credit_amount += transaction.amount
        else:
            debit_amount += transaction.amount

    available_balance = credit_amount+debit_amount
    context = {'available_balance' : available_balance, 'tracking_history' : tracking_history, 'credit_amount' : credit_amount, 'debit_amount' : debit_amount}
    return render(request, 'index.html', context)



def deleteTransaction(request, id):
    transaction = TrackingHistory.objects.filter(id = id)
    transaction.delete()
    return redirect('/')