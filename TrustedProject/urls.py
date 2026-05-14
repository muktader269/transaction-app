from django.contrib import admin
from django.urls import path
from circles import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.circle_list, name='circle_list'),
    path('create/', views.create_circle, name='create_circle'),
    path('update/<int:pk>/', views.update_circle, name='update_circle'),
    path('delete/<int:pk>/', views.delete_circle, name='delete_circle'),

    # মেম্বার ম্যানেজমেন্ট
    path('add-member/<int:circle_id>/', views.add_member, name='add_member'),
    path('delete-member/<int:member_id>/', views.delete_member, name='delete_member'),

    # এই লাইনটি মিসিং ছিল, তাই এরর দিচ্ছিল
    path('send-request/<int:circle_id>/', views.send_request, name='send_request'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)