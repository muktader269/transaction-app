from django.shortcuts import render, redirect
from .models import Transaction
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):

    history = Transaction.objects.filter(sender=request.user).order_by('-timestamp')

    if request.method == "POST":
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        mood = request.POST.get('mood')

        if phone and amount:

            Transaction.objects.create(
                sender=request.user,
                receiver_phone=phone,
                amount=amount,
                mood=mood
            )
            return redirect('dashboard')

    return render(request, 'my_transaction.html', {'history': history})