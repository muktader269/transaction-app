from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('myproject.urls')),

    path('transactions/', include('transaction.urls'), name='user_transactions'),
    path('savings/', include('SavingGoals.fintrackpro.savinggoals.urls'), name='user_savings'),
    path('trusted-circle/', include('circles.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)