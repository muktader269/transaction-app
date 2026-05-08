from django.shortcuts import render, redirect
from .models import Transaction
from django.contrib.auth.decorators import login_required


@login_required  
def dashboard(request):
    # History (Read operation)
    history = Transaction.objects.filter(sender=request.user).order_by('-timestamp')

    if request.method == "POST":
        # Send Money (Create operation)
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')

        if phone and amount:
            Transaction.objects.create(
                sender=request.user,
                receiver_phone=phone,
                amount=amount
            )
            return redirect('dashboard')

    return render(request, 'dashboard.html', {'history': history})