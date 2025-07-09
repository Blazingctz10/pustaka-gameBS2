from django.urls import path
from . import views

urlpatterns = [
    # Path untuk halaman utama, filter, dan pencarian
    path('', views.home, name='home'),
    path('kategori/<str:nama_kategori>/', views.home, name='games_by_category'),
    
    # Path untuk halaman lain di aplikasi catalog
    path('game/<int:pk>/', views.detail_game, name='detail_game'),
    path('game/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('game/<int:pk>/add_rating/', views.add_rating, name='add_rating'),
]