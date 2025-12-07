# 🥫 Manajer Persediaan Dapur (Python + SQLite)

Program ini merupakan aplikasi sederhana berbasis **CLI (Command Line Interface)** yang digunakan untuk mengelola persediaan bahan dapur.  
Aplikasi menyediakan fitur pencatatan stok, notifikasi bahan yang sudah kedaluwarsa, sorting data, hingga pengecekan bahan yang akan segera expired.

---

## 📌 Fitur Utama

### 🔔 Notifikasi Otomatis (Expired)
Saat program dijalankan, aplikasi otomatis menampilkan daftar bahan yang **sudah kadaluarsa**.

### ➕ Tambah Item
Menambahkan data bahan baru ke database, terdiri dari:
- Nama bahan
- Jumlah
- Tanggal kedaluwarsa

### 📋 Lihat Semua Persediaan
Menampilkan seluruh data persediaan dalam database.

### 🔃 Sorting Data
Pengguna dapat mengurutkan data berdasarkan:
- Nama
- Jumlah
- Tanggal kedaluwarsa

Dengan pilihan:
- **ASC** (Ascending)
- **DESC** (Descending)

### ✏ Edit Item
Mengubah data item berdasarkan ID:
- Nama baru
- Jumlah baru
- Tanggal kedaluwarsa baru

### 🗑 Hapus Item
Menghapus data item dari database berdasarkan ID.

### ⏳ Cek Item Hampir Kedaluwarsa
Menampilkan item yang akan expired dalam rentang hari tertentu yang dimasukkan pengguna.

---

## 🗂 Struktur Database (SQLite)

Database: `persediaan_dapur.db`  
Tabel: `persediaan`

| Kolom                 | Tipe Data | Keterangan                    |
|----------------------|-----------|-------------------------------|
| id                   | INTEGER   | Primary Key, Auto Increment   |
| nama                 | TEXT      | Nama bahan                    |
| jumlah               | INTEGER   | Jumlah persediaan             |
| tanggal_kedaluwarsa  | TEXT      | Format YYYY-MM-DD             |

---

## 🚀 Cara Menjalankan Program

1. Pastikan Python telah terinstal di komputer Anda.
2. Simpan file program, misalnya sebagai `dapur_manager.py`.
3. Jalankan program melalui terminal:

```bash
python dapur_manager.py


