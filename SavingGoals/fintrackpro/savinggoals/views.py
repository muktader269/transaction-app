from django.shortcuts import render, redirect, get_object_or_404
from .forms import SavingGoalsForm
from .models import SavingGoals
from decimal import Decimal

def home(request):
    save = SavingGoals.objects.all()
    return render(request, 'homee.html', {'save': save})

def create_savinggoals(request):
    if request.method == 'POST':
        form = SavingGoalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SavingGoalsForm()
    return render(request, 'forms.html', {'form': form})


def add_money(request, goal_id):
    if request.method == 'POST':
        goal = get_object_or_404(SavingGoals, id=goal_id)
        amount_to_add = request.POST.get('amount_to_add')
        if amount_to_add:
            try:

                goal.current_amount += Decimal(amount_to_add)
                goal.save()
            except:
                pass
    return redirect('home')


def delete_goal(request, goal_id):
    goal = get_object_or_404(SavingGoals, id=goal_id)
    goal.delete()
    return redirect('home')