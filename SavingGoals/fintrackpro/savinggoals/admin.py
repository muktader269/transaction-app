from django.contrib import admin
from .models import SavingGoals

@admin.register(SavingGoals)
class SavingGoalsAdmin(admin.ModelAdmin):
    list_display = ('goal_name', 'target_amount', 'current_amount', 'is_finished')
    list_filter = ('target_amount',)
    search_fields = ('goal_name',)