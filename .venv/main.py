 # main.py
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa
from data.mahasiswa import Mahasiswa

def main():
    view_mahasiswa = ViewMahasiswa()
    input_form = InputForm()

    while True:
        print("\nMenu Utama")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Ubah Data")
        print("4. Cari Data")
        print("5. Tampilkan List Data")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama = input_form.input_data()
            mahasiswa = Mahasiswa(nim, nama)
            view_mahasiswa.data_mahasiswa.tambah_data(mahasiswa)
        elif pilihan == "2":
            nim = input("Masukkan NIM yang akan dihapus: ")
            view_mahasiswa.data_mahasiswa.hapus_data(nim)
        elif pilihan == "3":
            nim = input("Masukkan NIM yang akan diubah: ")
            mahasiswa_baru = Mahasiswa(*input_form.input_data())
            view_mahasiswa.data_mahasiswa.ubah_data(nim, mahasiswa_baru)
        elif pilihan == "4":
            nim = input("Masukkan NIM yang dicari: ")
            view_mahasiswa.tampilkan_detail(nim)
        elif pilihan == "5":
            view_mahasiswa.tampilkan_list()
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "_main_":
    main()