[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Pustaka Game PGIR

Selamat datang di Pustaka Game PGIR, sebuah aplikasi web katalog game dinamis dan interaktif yang dibangun menggunakan framework Django. Proyek ini dirancang untuk menjadi platform komunitas di mana pengguna dapat menjelajahi, menilai, dan mendiskusikan berbagai macam game.

---

## ✨ Fitur Utama

Proyek ini dilengkapi dengan berbagai fitur modern untuk menciptakan pengalaman pengguna yang kaya dan profesional:

* **Sistem Katalog Game:**
    * Tampilan daftar game dalam format grid yang rapi.
    * **Pencarian Lanjutan:** Pencarian berdasarkan judul/deskripsi, filter berdasarkan developer, dan opsi untuk mengurutkan (sortir) berdasarkan game terbaru, judul, atau rating tertinggi.
    * **Pagination:** Halaman utama secara otomatis membagi daftar game menjadi beberapa halaman untuk performa yang cepat.
    * **Filter per Kategori:** Menampilkan game hanya dari kategori yang dipilih.

* **Sistem Pengguna & Profil:**
    * **Autentikasi Lengkap:** Alur untuk **Registrasi**, **Login**, dan **Logout** pengguna.
    * **Halaman Profil Personal:** Setiap pengguna memiliki halaman profil sendiri.
    * **Kustomisasi Profil:** Pengguna dapat mengunggah **gambar profil** dan menulis **bio** singkat.
    * **Statistik Pengguna:** Menampilkan jumlah total komentar dan rating yang telah diberikan.
    * **Status Pengguna:** Lencana status (Member, VIP, Admin) dengan warna berbeda untuk identifikasi visual.

* **Fitur Interaksi Sosial:**
    * **Sistem Rating Bintang:** Pengguna yang login dapat memberikan rating 1-5 bintang pada game. Rata-rata rating akan ditampilkan secara visual.
    * **Sistem Komentar:** Pengguna dapat meninggalkan komentar di setiap halaman detail game.
    * **Game Favorit:** Pengguna dapat menandai game sebagai favorit dan melihat daftar koleksi mereka di halaman profil.

* **Pengalaman Pengguna (UX) Modern:**
    * **Mode Terang & Gelap:** Tombol toggle untuk mengubah tema website secara instan, dengan pilihan yang tersimpan di browser.
    * **Logo Adaptif:** Logo website berubah secara otomatis mengikuti perubahan tema.
    * **Animasi Halus:** Efek animasi saat scroll (AOS), transisi antar halaman yang mulus (Swup), dan galeri gambar interaktif (GLightbox).
    * **Notifikasi "Flash":** Pesan konfirmasi yang informatif muncul setelah pengguna berhasil melakukan aksi (misalnya, setelah berkomentar atau registrasi).
    * **Desain Responsif:** Tampilan website beradaptasi dengan baik untuk perangkat desktop maupun mobile.

---

## 🛠️ Teknologi yang Digunakan

* **Backend:** Python, Django
* **Database:** PostgreSQL
* **Frontend:** HTML5, CSS3 (Flexbox, Grid, CSS Variables)
* **JavaScript Libraries:**
    * [AOS (Animate On Scroll)](https://michalsnik.github.io/aos/) - Untuk animasi saat scroll.
    * [Swup.js](https://swup.js.org/) - Untuk transisi halaman yang mulus.
    * [GLightbox](https://biati-digital.github.io/glightbox/) - Untuk galeri gambar interaktif.
* **Deployment:**
    * **Server Aplikasi:** Gunicorn
    * **Hosting PaaS (Rekomendasi):** Render

---

## 🚀 Instalasi & Setup Lokal

Berikut adalah langkah-langkah untuk menjalankan proyek ini di komputer lokal.

1.  **Clone Repository**
    ```bash
    git clone https://github.com/Blazingctz10/pustaka-gameBS2.git
    cd pustaka-gameBS2
    ```

2.  **Setup Database PostgreSQL**
    * Pastikan PostgreSQL sudah terinstall.
    * Buat database baru (misalnya, `SistemManajemenPerpusGame`).

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
    * Buat file `.env` di direktori utama proyek dan isi dengan kredensial Anda.
        ```
        SECRET_KEY='secret-key-anda'
        DEBUG=True
        DATABASE_URL='postgres://USER:PASSWORD@HOST:PORT/NAMA_DATABASE'
        ```

5.  **Jalankan Migrasi & Buat Superuser**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

6.  **Jalankan Server**
    ```bash
    python manage.py runserver
    ```
    Proyek sekarang berjalan di `http://127.0.0.1:8000/`.

---
## 📄 Lisensi

Bebas digunakan untuk pembelajaran dan pengembangan lebih lanjut.  

