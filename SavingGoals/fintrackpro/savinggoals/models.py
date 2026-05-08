from django.db import models
from django.core.validators import MinValueValidator


class SavingGoals(models.Model):
    goal_name = models.CharField(max_length=100)
    target_amount = models.DecimalField(decimal_places=2, max_digits=100)
    current_amount = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)

    def __str__(self):
        return self.goal_name

    @property
    def is_finished(self):
        return self.current_amount >= self.target_amount