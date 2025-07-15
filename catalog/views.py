from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from .models import Game, Komentar, Kategori, Profile, Rating
from .forms import RegisterForm, ProfileUpdateForm, RatingForm, UserUpdateForm
from django.core.paginator import Paginator
from django.contrib import messages

# View untuk Halaman Utama, Filter, Pencarian, dan Urutkan
def home(request, nama_kategori=None):
    judul_halaman = 'Choose Your Games !'
    game_list = Game.objects.prefetch_related('kategori').all()

    # --- Logika Filter Kategori ---
    if nama_kategori:
        kategori_obj = get_object_or_404(Kategori, nama_kategori=nama_kategori)
        game_list = game_list.filter(kategori=kategori_obj)
        judul_halaman = f"Game dalam Kategori: {kategori_obj.nama_kategori}"
    
    # --- Logika Advanced Filter ---
    developer_filter = request.GET.get('developer')
    if developer_filter and developer_filter != '':
        game_list = game_list.filter(developer__iexact=developer_filter)
        judul_halaman = f"Game oleh Developer: {developer_filter}"

    search_query = request.GET.get('q')
    if search_query:
        game_list = game_list.filter(
            Q(judul__icontains=search_query) | 
            Q(deskripsi__icontains=search_query)
        )
        judul_halaman = f"Hasil Pencarian untuk: '{search_query}'"

    # --- Logika untuk Mengurutkan (Sort By) ---
    sort_by = request.GET.get('sort')
    if sort_by == 'judul_asc':
        game_list = game_list.order_by('judul')
    elif sort_by == 'judul_desc':
        game_list = game_list.order_by('-judul')
    elif sort_by == 'rating_desc':
        game_list = game_list.annotate(avg_rating=Avg('ratings__skor')).order_by('-avg_rating')
    else: # Default
        game_list = game_list.order_by('-tanggal_ditambahkan')

    # Ambil daftar unik semua developer untuk dropdown
    developers = Game.objects.values_list('developer', flat=True).distinct().order_by('developer')

    # --- PAGINATION ---
    paginator = Paginator(game_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'judul_halaman': judul_halaman,
        'developers': developers,
        'selected_developer': developer_filter,
        'selected_sort': sort_by,
    }
    return render(request, 'catalog/home.html', context)


# --- Sisa view lainnya (detail_game, add_comment, add_rating, dll.) tetap sama ---

def detail_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    average_rating_data = game.ratings.aggregate(average=Avg('skor'))
    average_rating = average_rating_data.get('average') or 0
    rating_count = game.ratings.count()
    rating_form = RatingForm()
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = game in request.user.profile.favorit.all()
    context = {
        'game': game, 'judul_halaman': game.judul,
        'average_rating': average_rating, 'rating_count': rating_count,
        'rating_form': rating_form, 'is_favorited': is_favorited,
    }
    return render(request, 'catalog/detail_game.html', context)

@login_required
def add_comment(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        Komentar.objects.create(game=game, pengguna=request.user, isi_komentar=request.POST.get('isi_komentar'))
        messages.success(request, 'Komentar Anda berhasil ditambahkan!')
    return redirect('detail_game', pk=game.pk)

@login_required
def add_rating(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            existing_rating, created = Rating.objects.update_or_create(
                game=game, user=request.user, defaults={'skor': form.cleaned_data['skor']}
            )
            if created: messages.success(request, 'Terima kasih telah memberikan rating!')
            else: messages.success(request, 'Rating Anda berhasil diperbarui!')
    return redirect('detail_game', pk=game.pk)

@login_required
def toggle_favorite(request, pk):
    game = get_object_or_404(Game, pk=pk)
    profile = request.user.profile
    if game in profile.favorit.all():
        profile.favorit.remove(game)
        messages.info(request, f'"{game.judul}" telah dihapus dari daftar favorit Anda.')
    else:
        profile.favorit.add(game)
        messages.success(request, f'"{game.judul}" telah ditambahkan ke daftar favorit Anda!')
    return redirect('detail_game', pk=pk)

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
    context = {'form': form, 'judul_halaman': 'Buat Akun Baru'}
    return render(request, 'registration/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profil Anda berhasil diperbarui!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    user_comments = Komentar.objects.filter(pengguna=request.user).order_by('-tanggal_dibuat')
    total_ratings_given = Rating.objects.filter(user=request.user).count()
    context = {
        'judul_halaman': f'Profile Pengguna: {request.user.username}',
        'user_comments': user_comments,
        'u_form': u_form, 'p_form': p_form,
        'total_ratings_given': total_ratings_given,
    }
    return render(request, 'catalog/profile.html', context)