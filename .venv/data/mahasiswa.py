# data/mahasiswa.py
class Mahasiswa:
    def _init_(self, nim, nama):
        self.nim = nim
        self.nama = nama

class DataMahasiswa:
    def _init_(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_data(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah_data(self, nim, mahasiswa_baru):
        for idx, mahasiswa in enumerate(self.data):
            if mahasiswa.nim == nim:
                self.data[idx] = mahasiswa_baru

    def cari_data(self, nim):
        for mahasiswa in self.data:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None