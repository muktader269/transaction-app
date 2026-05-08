from django import forms
from .models import SavingGoals

class SavingGoalsForm(forms.ModelForm):
    class Meta:
        model = SavingGoals
        fields = ['goal_name', 'target_amount']