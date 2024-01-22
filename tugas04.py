# Import modul yang dibutuhkan
import datetime

# Definisikan fungsi untuk menambahkan todo
def tambah_todo(todo):
    # Buka file todo
    with open("todo.txt", "a") as file:
        # Tulis todo ke file
        file.write(todo + "\n")

# Definisikan fungsi untuk menghapus todo
def hapus_todo(id):
    # Buka file todo
    with open("todo.txt", "r") as file:
        # Baca data todo
        data = file.readlines()

    # Hapus todo dengan id yang ditentukan
    for i, line in enumerate(data):
        if line.startswith(id):
            data.pop(i)
            break

    # Tulis ulang data todo ke file
    with open("todo.txt", "w") as file:
        for line in data:
            file.write(line)

# Definisikan fungsi untuk menampilkan todo
def tampilkan_todo():
    # Buka file todo
    with open("todo.txt", "r") as file:
        # Baca data todo
        data = file.readlines()

    # Tampilkan todo
    for line in data:
        print(line.strip())

# Program utama
while True:
    # Tampilkan menu
    print("=======================")
    print("   PROGRAM TODO LIST")
    print("=======================")
    print("Menu:")
    print("1. Tambah todo")
    print("2. Hapus todo")
    print("3. Tampilkan todo")
    print("4. Keluar")

    # Pilih menu
    menu = input("Pilih menu: ")

    # Proses menu
    if menu == "1":
        # Tambah todo
        todo = input("Tambah todo: ")
        tambah_todo(todo)
    elif menu == "2":
        # Hapus todo
        id = input("Hapus todo dengan id: ")
        hapus_todo(id)
    elif menu == "3":
        # Tampilkan todo
        tampilkan_todo()
    elif menu == "4":
        # Mengakhiri program
        break
