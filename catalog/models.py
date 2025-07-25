# PROYEKGAME/catalog/models.py

from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static # Pastikan import ini ada

# ... (model Kategori, Game, Screenshot, DownloadLink, Komentar) ...
class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=50, unique=True)
    def __str__(self): return self.nama_kategori
    class Meta: verbose_name_plural = "Kategori"

class Game(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField(blank=True, null=True)
    versi = models.CharField(max_length=50, blank=True)
    developer = models.CharField(max_length=100, blank=True)
    gambar_utama_url = models.URLField(max_length=500, blank=True)
    tanggal_ditambahkan = models.DateTimeField(auto_now_add=True)
    jumlah_dilihat = models.PositiveIntegerField(default=0)
    kategori = models.ManyToManyField(Kategori, related_name="games")
    def __str__(self): return self.judul

class Screenshot(models.Model):
    game = models.ForeignKey(Game, related_name='screenshots', on_delete=models.CASCADE)
    url_gambar = models.URLField(max_length=500)
    caption = models.CharField(max_length=255, blank=True)
    def __str__(self): return f"Screenshot untuk {self.game.judul}"

class DownloadLink(models.Model):
    game = models.ForeignKey(Game, related_name='download_links', on_delete=models.CASCADE)
    nama_link = models.CharField(max_length=100)
    url_link = models.URLField(max_length=500)
    def __str__(self): return f"{self.nama_link} for {self.game.judul}"

class Komentar(models.Model):
    game = models.ForeignKey(Game, related_name='komentars', on_delete=models.CASCADE)
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='balasan', on_delete=models.CASCADE)
    isi_komentar = models.TextField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Komentar by {self.pengguna.username} on {self.game.judul}"

class Profile(models.Model):
    USER_TYPE_CHOICES = (("member", "Member"), ("vip", "VIP Member"), ("admin", "Admin"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipe_user = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="member")
    gambar = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, help_text="Ceritakan sedikit tentang diri Anda.")
    favorit = models.ManyToManyField(Game, blank=True, related_name="difavoritkan_oleh")

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def gambar_url(self):
        try:
            url = self.gambar.url
        except (ValueError, AttributeError):
            url = static('catalog/img/default.jpg')
        return url

class Rating(models.Model):
    game = models.ForeignKey(Game, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    skor = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    class Meta:
        unique_together = ('game', 'user')
    def __str__(self):
        return f"{self.skor} bintang untuk {self.game.judul} oleh {self.user.username}"