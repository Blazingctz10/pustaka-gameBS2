# Lokasi: catalog/views.py (Versi Final dengan Filter & Pencarian)

# ===============================================================
# BAGIAN 1: IMPORT
# ===============================================================
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # <--- PENTING: Import untuk pencarian
from .models import Game, Komentar, Kategori  # <--- PENTING: Pastikan Kategori ada di sini
from .forms import RegisterForm, ProfileUpdateForm
# ===============================================================
# BAGIAN 2: KUMPULAN VIEW
# ===============================================================

# View untuk Halaman Utama, Filter Kategori, dan Pencarian
def home(request, nama_kategori=None):
    judul_halaman = 'YAZID GAME CATALOG !'
    # Ambil semua game sebagai dasar
    daftar_game = Game.objects.all().order_by('-tanggal_ditambahkan')

    # --- LOGIKA FILTER BERDASARKAN KATEGORI ---
    if nama_kategori:
        kategori_obj = get_object_or_404(Kategori, nama_kategori=nama_kategori)
        daftar_game = daftar_game.filter(kategori=kategori_obj)
        judul_halaman = f"Game dalam Kategori: {kategori_obj.nama_kategori}"

    # --- LOGIKA PENCARIAN (SEARCH) ---
    search_query = request.GET.get('q')
    if search_query:
        # Filter queryset yang sudah ada (baik semua game atau yang sudah difilter per kategori)
        daftar_game = daftar_game.filter(
            Q(judul__icontains=search_query) |
            Q(deskripsi__icontains=search_query)
        )
        judul_halaman = f"Hasil Pencarian untuk: '{search_query}'"

    # Siapkan data untuk dikirim ke template
    context = {
        'daftar_game': daftar_game,
        'judul_halaman': judul_halaman,
    }
    return render(request, 'catalog/home.html', context)


# View untuk Halaman Detail Game (Tidak ada perubahan)
def detail_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    context = {
        'game': game,
        'judul_halaman': game.judul
    }
    return render(request, 'catalog/detail_game.html', context)


# View untuk Menambah Komentar (Tidak ada perubahan)
@login_required
def add_comment(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        Komentar.objects.create(
            game=game,
            pengguna=request.user,
            isi_komentar=request.POST.get('isi_komentar')
        )
    return redirect('detail_game', pk=game.pk)


# View untuk Halaman Registrasi (Tidak ada perubahan)
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    context = {
        'form': form,
        'judul_halaman': 'Buat Akun Baru'
    }
    return render(request, 'registration/register.html', context)

@login_required
def profile(request):
    # Ambil semua komentar yang dibuat oleh user yang sedang login
    user_comments = Komentar.objects.filter(pengguna=request.user).order_by('-tanggal_dibuat')
    
    context = {
        'judul_halaman': f'Profile Pengguna: {request.user.username}',
        'user_comments': user_comments
    }
    return render(request, 'catalog/profile.html', context)

@login_required
def profile(request):
    # --- Logika untuk memproses form update ---
    if request.method == 'POST':
        # request.FILES diperlukan untuk menangani upload file/gambar
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile') # Redirect kembali ke halaman profil
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    # --- Akhir dari logika form ---

    user_comments = Komentar.objects.filter(pengguna=request.user).order_by('-tanggal_dibuat')
    
    context = {
        'judul_halaman': f'Profile Pengguna: {request.user.username}',
        'user_comments': user_comments,
        'p_form': p_form # <-- Kirim form ke template
    }
    return render(request, 'catalog/profile.html', context)