
from django.contrib import admin
from django.urls import path
from card import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wishing/', views.wishing_card, name='wishing'),
    path('wishing/<int:pk>/', views.wishing_card, name='wishing'),
    path('create/', views.create_card, name='create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
