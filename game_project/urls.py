# PROYEKGAME/game_project/urls.py (Versi Final & Benar)

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. URL untuk Admin Django
    path('admin/', admin.site.urls),

    # 2. URL untuk semua halaman utama kita (home, detail, profile, etc.)
    path('', include('catalog.urls')),

    # 3. URL Otentikasi yang diatur secara manual agar tidak bentrok
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),
        name='account_logout' # Menggunakan nama unik untuk menghindari tabrakan
    ),
]

# 4. Pengaturan untuk menyajikan file media (gambar profil) saat pengembangan
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)