from abc import ABC, abstractmethod

class Manusia(ABC):
    def Manusia__init__(self, nama, nim, umur, prodi):
        self.nama = nama
        self.nim = nim
        self.umur = umur
        self.prodi = prodi
    
    @abstractmethod
    def input_data(self, nama, nim, umur, prodi):
        pass
    
    @abstractmethod
    def tampilkan_detail(self):
        pass

class Mahasiswa(Manusia):
    def input_data(self, nama, nim, umur, prodi):
        if not isinstance(nama, str):
            raise TypeError("Nama harus berupa string")
        if not isinstance(nim, str):
            raise TypeError("NIM harus berupa string")
        if not isinstance(umur, int):
            raise TypeError("Umur harus berupa integer")
        if not isinstance(prodi, str):
            raise TypeError("Prodi harus berupa string")
        
        if len(nim) != 8 or not nim.isdigit():
            raise ValueError("NIM harus berupa 8 digit angka")
        if umur < 17 or umur > 40:
            raise ValueError("Umur harus antara 17 sampai 40 tahun")
        
        self.nama = nama
        self.nim = nim
        self.umur = umur
        self.prodi = prodi
    
    def tampilkan_detail(self):
        print("Detail Mahasiswa:")
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Umur:", self.umur)
        print("Prodi:", self.prodi)

try:
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa (8 digit angka): ")
    umur = int(input("Masukkan umur mahasiswa: "))
    prodi = input("Masukkan program studi mahasiswa: ")

    mhs = Mahasiswa()
    mhs.input_data(nama, nim, umur, prodi)
    mhs.tampilkan_detail()
except (TypeError, ValueError) as e:
    print("Error:", e)