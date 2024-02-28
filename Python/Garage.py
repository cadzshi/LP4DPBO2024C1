#import library
from ParkingLot import ParkingLot

#deklarasi class
class Garage:
    #private atribut
    __namaGarasi = ""
    __luasGarasi = ""
    __daftarKendaraan = ""
    __parking = []
    

    #constructor
    def __init__(self, namaGarasi = "", luasGarasi = "", daftarKendaraan = ""):
        self.__namaGarasi = namaGarasi
        self.__luasGarasi = luasGarasi
        self.__daftarKendaraan = daftarKendaraan
        self.__parking = []
    
    #setter
    def setnamaGarasi(self, namaGarasi):
        self.__namaGarasi = namaGarasi
    def setluasGarasi(self, luasGarasi):
        self.__luasGarasi = luasGarasi
    def setdaftarKendaraan(self, daftarKendaraan):
        self.__daftarKendaraan = daftarKendaraan
    def setparking(self, parking):
        self.__parking.append(parking)
    
    #getter
    def getnamaGarasi(self):
        return self.__namaGarasi
    def getluasGarasi(self):
        return self.__luasGarasi
    def getdaftarKendaraan(self):
        return self.__daftarKendaraan
    def getparking(self):
        return self.__parking

