from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('myproject.urls')),

    
    path('transactions/', include('transaction.urls'), name='user_transactions'),
    path('savings/', include('SavingGoals.fintrackpro.savinggoals.urls'), name='user_savings'),
]