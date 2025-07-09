# PROYEKGAME/game_project/urls.py (Versi Final & Benar)

from django.contrib import admin
from django.urls import path, include

# Import yang dibutuhkan
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. URL untuk Admin Django
    path('admin/', admin.site.urls),

    # 2. URL untuk semua halaman utama kita
    path('', include('catalog.urls')),

    # 3. URL Otentikasi yang diatur secara manual
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),
        name='account_logout'
    ),
]

# ▼▼▼ PASTIKAN BLOK KODE INI ADA DI BAGIAN PALING BAWAH ▼▼▼
# Blok ini hanya aktif saat mode DEBUG=True (pengembangan)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)