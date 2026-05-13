from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_money')
    receiver_phone = models.CharField(max_length=11)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    mood = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} to {self.receiver_phone} - {self.amount} TK"