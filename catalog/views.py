# Lokasi: catalog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from .models import Game, Komentar, Kategori, Profile, Rating
from .forms import RegisterForm, ProfileUpdateForm, RatingForm 
from django.core.paginator import Paginator
from django.contrib import messages

# View untuk Halaman Utama, Filter, Pencarian, dan Pagination
def home(request, nama_kategori=None):
    judul_halaman = 'Choose Your Games !'
    game_list = Game.objects.prefetch_related('kategori').all().order_by('-tanggal_ditambahkan')
    
    if nama_kategori:
        kategori_obj = get_object_or_404(Kategori, nama_kategori=nama_kategori)
        game_list = game_list.filter(kategori=kategori_obj)
        judul_halaman = f"Game dalam Kategori: {kategori_obj.nama_kategori}"
    
    search_query = request.GET.get('q')
    if search_query:
        game_list = game_list.filter(
            Q(judul__icontains=search_query) | 
            Q(deskripsi__icontains=search_query)
        )
        judul_halaman = f"Hasil Pencarian untuk: '{search_query}'"

    paginator = Paginator(game_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'judul_halaman': judul_halaman,
    }
    return render(request, 'catalog/home.html', context)


# View untuk Halaman Detail Game
def detail_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    average_rating_data = game.ratings.aggregate(average=Avg('skor'))
    average_rating = average_rating_data.get('average') or 0
    rating_count = game.ratings.count()
    
    # Menyiapkan form rating untuk ditampilkan
    rating_form = RatingForm()

    context = {
        'game': game,
        'judul_halaman': game.judul,
        'average_rating': average_rating,
        'rating_count': rating_count,
        'rating_form': rating_form, # Kirim form ke template
    }
    return render(request, 'catalog/detail_game.html', context)


# View untuk Menambah Komentar
@login_required
def add_comment(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        Komentar.objects.create(
            game=game,
            pengguna=request.user,
            isi_komentar=request.POST.get('isi_komentar')
        )
        messages.success(request, 'Komentar Anda berhasil ditambahkan!')
    return redirect('detail_game', pk=game.pk)

# View untuk Menambah/Mengubah Rating
@login_required
def add_rating(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            # Cek apakah user sudah pernah memberi rating untuk game ini
            existing_rating, created = Rating.objects.update_or_create(
                game=game, 
                user=request.user,
                defaults={'skor': form.cleaned_data['skor']}
            )
            if created:
                messages.success(request, 'Terima kasih telah memberikan rating!')
            else:
                messages.success(request, 'Rating Anda berhasil diperbarui!')
    return redirect('detail_game', pk=game.pk)


# View untuk Halaman Registrasi
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Akun berhasil dibuat! Selamat datang, {user.username}!')
            return redirect('home')
    else:
        form = RegisterForm()

    context = {
        'form': form,
        'judul_halaman': 'Buat Akun Baru'
    }
    return render(request, 'registration/register.html', context)


# View untuk Halaman Profile
@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Profil Anda berhasil diperbarui!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    user_comments = Komentar.objects.filter(pengguna=request.user).order_by('-tanggal_dibuat')
    
    context = {
        'judul_halaman': f'Profile Pengguna: {request.user.username}',
        'user_comments': user_comments,
        'p_form': p_form
    }
    return render(request, 'catalog/profile.html', context)