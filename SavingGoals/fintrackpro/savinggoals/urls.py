from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_savinggoals, name='create_savinggoals'),
    path('add_money/<int:goal_id>/', views.add_money, name='add_money'),
    path('delete_goal/<int:goal_id>/', views.delete_goal, name='delete_goal'),
]