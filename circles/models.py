from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Circle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    cover_image = models.ImageField(upload_to='circle_covers/', null=True, blank=True, default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} in {self.circle.name}"

class TrustedRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_reqs')
    receiver_email = models.EmailField()
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)