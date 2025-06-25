# 🕹️ Pustaka Game (BS2)

**Pustaka Game** adalah aplikasi web berbasis Django yang dibuat sebagai tugas akhir mata kuliah Basis Data 2. Aplikasi ini memungkinkan pengguna menjelajahi koleksi game, mencari berdasarkan kategori, serta memiliki profil pribadi dengan gambar.

---

## 🚀 Fitur Utama

- 🔐 Registrasi, login, logout
- 📂 Filter kategori dan pencarian dinamis
- 🖼️ Upload & update gambar profil
- 🎨 Desain "Dark Elegant" dengan CSS modern (Flexbox, Grid, CSS Variables)
- 🧠 Signals untuk auto-create profil saat user dibuat
- ⚡ Optimisasi query dengan ORM
- 🌍 Siap untuk deployment (misalnya ke Render)

---

## 🛠️ Instalasi & Menjalankan Proyek

### 1. Clone repository ini

```bash
git clone https://github.com/Blazingctz10/pustaka-gameBS2.git
cd pustaka-gameBS2
```

### 2. Buat dan aktifkan virtual environment

```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Mac/Linux:
source .venv/bin/activate
```

### 3. Install dependensi

```bash
pip install -r requirements.txt
```

### 4. Migrasi database

```bash
python manage.py migrate
```

### 5. Jalankan server lokal

```bash
python manage.py runserver
```

Akses di browser: [http://localhost:8000](http://localhost:8000)

---

## 📁 Struktur Folder

```
pustaka-gameBS2/
├── catalog/
│   ├── models.py, views.py, signals.py
│   ├── static/, templates/
├── game_project/
│   ├── settings.py, urls.py
├── media/
├── requirements.txt
├── .gitignore
└── manage.py
```

---

## 👥 Kontributor

Proyek ini dikembangkan oleh kelompok Basis Data 2  
💡 Untuk pembelajaran Django & deployment web modern.

---

## 📄 Lisensi

Bebas digunakan untuk pembelajaran dan pengembangan lebih lanjut.  
Tambahkan lisensi jika dibutuhkan.
