[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Pustaka Game YAJIZ

Selamat datang di Pustaka Game YAJIZ, sebuah aplikasi web katalog game yang dibangun menggunakan Django. Proyek ini memungkinkan pengguna untuk menjelajahi, mencari, memfilter, dan berinteraksi dengan koleksi game melalui sistem komentar dan rating.

![Screenshot Halaman Utama]([https://i.imgur.com/your-screenshot-link.png](https://imgur.com/a/6phaKJP))


---

## ✨ Fitur Utama

Proyek ini dilengkapi dengan berbagai fitur modern untuk menciptakan pengalaman pengguna yang kaya dan interaktif:

* **Autentikasi Pengguna:** Sistem lengkap untuk **Registrasi**, **Login**, dan **Logout**.
* **Profil Pengguna:** Setiap pengguna memiliki halaman profil sendiri dengan **gambar profil yang bisa diunggah** dan riwayat komentar.
* **Katalog Game:** Menampilkan daftar game dengan **Pagination** (penomoran halaman) agar tidak membebani halaman.
* **Filter & Pencarian:** Pengguna dapat **memfilter** game berdasarkan kategori dan melakukan **pencarian** berdasarkan judul atau deskripsi.
* **Sistem Interaksi:**
    * **Komentar:** Pengguna yang sudah login dapat meninggalkan komentar di halaman detail game.
    * **Rating Bintang:** Pengguna bisa memberikan rating 1-5 bintang untuk setiap game, dan rata-rata rating akan ditampilkan.
* **Tampilan Modern & Elegan:**
    * Tema **"Dark Elegant"** yang konsisten di seluruh website.
    * **Animasi Halus:** Efek animasi saat scroll (AOS), transisi antar halaman yang mulus (Swup), dan galeri gambar interaktif (GLightbox).
    * **Desain Responsif:** Tampilan beradaptasi dengan baik di perangkat desktop maupun mobile.

---

## 🛠️ Teknologi yang Digunakan

* **Backend:** Python, Django
* **Database:** PostgreSQL
* **Frontend:** HTML5, CSS3 (Flexbox, Grid, CSS Variables)
* **JavaScript Libraries:**
    * [AOS (Animate On Scroll)](https://michalsnik.github.io/aos/) - Untuk animasi saat scroll.
    * [Swup.js](https://swup.js.org/) - Untuk transisi halaman yang mulus.
    * [GLightbox](https://biati-digital.github.io/glightbox/) - Untuk galeri gambar interaktif.
* **Deployment (Rencana):** Gunicorn, Render (PaaS)

---

## 🚀 Instalasi & Setup Lokal

Berikut adalah langkah-langkah untuk menjalankan proyek ini di komputer lokal.

1.  **Clone Repository**
    ```bash
    git clone [https://github.com/Blazingctz10/pustaka-gameBS2.git](https://github.com/Blazingctz10/pustaka-gameBS2.git)
    cd pustaka-gameBS2
    ```

2.  **Setup Database PostgreSQL**
    * Pastikan PostgreSQL sudah terinstall di sistem Anda.
    * Buat database dan user baru. Contoh:
        ```sql
        CREATE DATABASE "SistemManajemenPerpusGame";
        CREATE USER postgres WITH PASSWORD '12345';
        GRANT ALL PRIVILEGES ON DATABASE "SistemManajemenPerpusGame" TO postgres;
        ```

3.  **Buat Virtual Environment & Install Dependencies**
    ```bash
    # Buat venv
    python -m venv .venv

    # Aktifkan venv (Windows)
    .venv\Scripts\activate

    # Install semua library yang dibutuhkan
    pip install -r requirements.txt
    ```

4.  **Konfigurasi Environment Variables**
    * Salin atau buat ulang file `.env.example` menjadi `.env`.
    * Isi file `.env` dengan kredensial Anda. File ini **tidak boleh** di-commit ke GitHub.
        ```
        # Contoh isi file .env
        SECRET_KEY='secret-key-anda-yang-sangat-rahasia'
        DEBUG=True
        DATABASE_URL='postgres://postgres:12345@localhost:5432/SistemManajemenPerpusGame'
        ```
    * *Catatan: Anda mungkin perlu mengubah file `settings.py` untuk membaca variabel ini menggunakan library seperti `python-decouple`.*

5.  **Jalankan Migrasi Database**
    Perintah ini akan membuat semua tabel di database baru Anda.
    ```bash
    python manage.py migrate
    ```

6.  **Buat Akun Superuser**
    Akun ini digunakan untuk mengakses halaman admin Django.
    ```bash
    python manage.py createsuperuser
    ```

7.  **Jalankan Server**
    ```bash
    python manage.py runserver
    ```
    Sekarang proyek sudah berjalan di `http://127.0.0.1:8000/`.

---

## ☁️ Catatan Deployment

Proyek ini sudah dikonfigurasi untuk bisa di-deploy dengan mudah ke layanan PaaS seperti **Render**.
* **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
* **Start Command:** `gunicorn game_project.wsgi`

---
## 📄 Lisensi

Bebas digunakan untuk pembelajaran dan pengembangan lebih lanjut.  

