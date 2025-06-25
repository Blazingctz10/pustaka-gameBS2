# PROYEKGAME/catalog/admin.py

from django.contrib import admin
from django.contrib.auth.models import User
from .models import Kategori, Game, Screenshot, DownloadLink, Komentar, Profile # Tambahkan Profile di sini

admin.site.register(Kategori)
admin.site.register(Game)
admin.site.register(Screenshot)
admin.site.register(DownloadLink)
admin.site.register(Komentar)
admin.site.register(Profile) # Daftarkan Profile di sini