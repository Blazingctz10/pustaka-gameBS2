from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kategori/<str:nama_kategori>/', views.home, name='games_by_category'),
    path('game/<int:pk>/', views.detail_game, name='detail_game'),
    path('game/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('game/<int:pk>/add_rating/', views.add_rating, name='add_rating'),
    # ▼▼▼ TAMBAHAN BARU ▼▼▼
    path('game/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
]