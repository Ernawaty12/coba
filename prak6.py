from abc import ABC, abstractmethod

class ttg_interface_manusia(ABC):
   
    @abstractmethod
    def Berjalan(self):
        pass
    @abstractmethod
    def berlari(self,jarak):
        pass

class atlit(ttg_interface_manusia):
    def Berjalan(self):
        print("Aku Atlit, aku mampu berjalan")

    def berlari(self, jarak):
        print("Aku atlit. aku mampu berlari sejauh", jarak, "km")

class petani(ttg_interface_manusia):
    def Berjalan(self):
        print("Aku petani. aku mampu berjalan")

    def berlari(self, jarak):
        print("Aku petani. aku mampu berlari sejauh", jarak, "km")
Etwar=atlit()

paidi=petani()

Etwar.Berjalan()
Etwar.berlari(42)

paidi.Berjalan()
paidi.berlari(10)



def hitung_luas_persegi(sisi):
    try:
        return sisi * sisi
    except TypeError:
        return 'Type data yang anda masukan tidak sesuai !!!'
    
sisi = input('masukan sisi : ')
persegi = hitung_luas_persegi(sisi)
print(persegi)