# view/mahasiswa.py
from data.mahasiswa import DataMahasiswa

class ViewMahasiswa:
    def _init_(self):
        self.data_mahasiswa = DataMahasiswa()

    def tampilkan_list(self):
        for mahasiswa in self.data_mahasiswa.data:
            print(f"NIM: {mahasiswa.nim}, Nama: {mahasiswa.nama}")

    def tampilkan_detail(self, nim):
        mahasiswa = self.data_mahasiswa.cari_data(nim)
        if mahasiswa:
            print(f"Detail Mahasiswa - NIM: {mahasiswa.nim}, Nama: {mahasiswa.nama}")
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")