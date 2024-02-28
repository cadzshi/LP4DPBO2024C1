#import library
from Vehicle import Vehicle

#deklarasi class
class Car(Vehicle):

    #private atribut
    __jmlKursi = ""
    __jmlPintu = ""

    #constructor
    def __init__(self, jmlKursi = "", jmlPintu = ""):
        self.__jmlKursi = jmlKursi
        self.__jmlPintu = jmlPintu
    
    #setter
    def setjmlKursi(self, jmlKursi):
        self.__jmlKursi = jmlKursi
    def setjmlPintu(self, jmlPintu):
        self.__jmlPintu = jmlPintu
     
    #getter
    def getjmlKursi(self):
        return self.__jmlKursi
    def getjmlPintu(self):
        return self.__jmlPintu
    