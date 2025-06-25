# PROYEKGAME/catalog/urls.py (Versi Perbaikan)

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('kategori/<str:nama_kategori>/', views.home, name='games_by_category'),
    path('game/<int:pk>/', views.detail_game, name='detail_game'),
    path('game/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('register/', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)