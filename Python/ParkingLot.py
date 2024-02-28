#deklarasi class
class ParkingLot:
    #private atribut
    __kapasitas = ""
    __jmlKendaraan = ""

    #constructor
    def __init__(self, kapasitas = "", jmlKendaraan = ""):
        self.__kapasitas = kapasitas
        self.__jmlKendaraan = jmlKendaraan

    #setter
    def setkapasitas(self, kapasitas):
        self.__kapasitas = kapasitas
    def setjmlKendaraan(self, jmlKendaraan):
        self.__jmlKendaraan = jmlKendaraan
        
    #getter
    def getkapasitas(self):
        return self.__kapasitas
    def getjmlKendaraan(self):
        return self.__jmlKendaraan
    