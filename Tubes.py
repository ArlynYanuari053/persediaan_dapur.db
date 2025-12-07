import sqlite3
from datetime import datetime, timedelta

# ===============================
# 1. KONEKSI DATABASE
# ===============================
conn = sqlite3.connect("persediaan_dapur.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persediaan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    jumlah INTEGER NOT NULL,
    tanggal_kedaluwarsa TEXT NOT NULL
)
""")
conn.commit()


# ===============================
# FUNGSI NOTIFIKASI EXPIRED
# ===============================
def notif_expired():
    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT * FROM persediaan
        WHERE tanggal_kedaluwarsa < ?
    """, (today,))

    expired_items = cursor.fetchall()

    print("\n===== NOTIFIKASI EXPIRED =====")
    if not expired_items:
        print("✔ Tidak ada item yang expired.\n")
        return

    print("⚠ Item yang sudah expired:")
    for item in expired_items:
        print(f"ID: {item[0]} | {item[1]} | Exp: {item[3]}")
    print()


# ===============================
# 2. FUNGSI-FUNGSI CRUD
# ===============================
def tambah_item():
    nama = input("Nama bahan: ")
    jumlah = int(input("Jumlah: "))
    tanggal = input("Tanggal kedaluwarsa (YYYY-MM-DD): ")

    cursor.execute("""
        INSERT INTO persediaan (nama, jumlah, tanggal_kedaluwarsa) 
        VALUES (?, ?, ?)
    """, (nama, jumlah, tanggal))

    conn.commit()
    print("✔ Item berhasil ditambahkan!\n")


def lihat_semua(order_by="id", ascending=True):
    direction = "ASC" if ascending else "DESC"
    query = f"SELECT * FROM persediaan ORDER BY {order_by} {direction}"

    cursor.execute(query)
    data = cursor.fetchall()

    if not data:
        print("Tidak ada persediaan.\n")
        return

    print("\n=== DAFTAR PERSEDIAAN ===")
    for item in data:
        print(f"ID: {item[0]} | {item[1]} | Jumlah: {item[2]} | Exp: {item[3]}")
    print()


def menu_sorting():
    print("""
=== SORTING PERSEDIAAN ===
1. Sort berdasarkan nama
2. Sort berdasarkan tanggal kedaluwarsa
3. Sort berdasarkan jumlah
    """)

    pilih = input("Pilih jenis sorting: ")

    print("Urutan: 1. ASCENDING  |  2. DESCENDING")
    urut = input("Pilih: ")

    ascending = True if urut == "1" else False

    if pilih == "1":
        lihat_semua(order_by="nama", ascending=ascending)
    elif pilih == "2":
        lihat_semua(order_by="tanggal_kedaluwarsa", ascending=ascending)
    elif pilih == "3":
        lihat_semua(order_by="jumlah", ascending=ascending)
    else:
        print("Pilihan tidak valid!")


def edit_item():
    lihat_semua()
    id_item = int(input("Masukkan ID item yang ingin diedit: "))

    nama = input("Nama baru: ")
    jumlah = int(input("Jumlah baru: "))
    tanggal = input("Tanggal kedaluwarsa baru (YYYY-MM-DD): ")

    cursor.execute("""
        UPDATE persediaan
        SET nama=?, jumlah=?, tanggal_kedaluwarsa=?
        WHERE id=?
    """, (nama, jumlah, tanggal, id_item))

    conn.commit()
    print("✔ Item berhasil diperbarui!\n")


def hapus_item():
    lihat_semua()
    id_item = int(input("Masukkan ID item yang ingin dihapus: "))

    cursor.execute("DELETE FROM persediaan WHERE id=?", (id_item,))
    conn.commit()

    print("✔ Item berhasil dihapus!\n")


def cek_kedaluwarsa():
    hari = int(input("Cek item yang akan kedaluwarsa dalam berapa hari? "))
    batas = datetime.now() + timedelta(days=hari)

    cursor.execute("""
        SELECT * FROM persediaan 
        WHERE tanggal_kedaluwarsa <= ?
    """, (batas.strftime("%Y-%m-%d"),))

    data = cursor.fetchall()

    print(f"\n=== ITEM YANG KEDALUWARSA DALAM {hari} HARI ===")
    if not data:
        print("Tidak ada item yang akan kedaluwarsa.\n")
        return

    for item in data:
        print(f"ID: {item[0]} | {item[1]} | exp: {item[3]}")
    print()


# ===============================
# 3. MENU UTAMA
# ===============================
def menu():
    notif_expired()  # 🔔 Notifikasi otomatis setiap program dibuka

    while True:
        print("""
==== MANAJER PERSEDIAAN DAPUR ====
1. Tambah item
2. Lihat semua persediaan
3. Sorting data
4. Edit item
5. Hapus item
6. Cek item yang hampir kedaluwarsa
7. Keluar
""")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_item()
        elif pilihan == "2":
            lihat_semua()
        elif pilihan == "3":
            menu_sorting()
        elif pilihan == "4":
            edit_item()
        elif pilihan == "5":
            hapus_item()
        elif pilihan == "6":
            cek_kedaluwarsa()
        elif pilihan == "7":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!\n")


# ===============================
# 4. JALANKAN PROGRAM
# ===============================
menu()
conn.close()
