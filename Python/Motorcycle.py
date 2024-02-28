#import library
from Vehicle import Vehicle

#deklarasi class
class Motorcycle(Vehicle):

    #private atribut
    __jnsMotor = ""
    __jmlTangki = ""

    #constructor
    def __init__(self, jnsMotor = "", jmlTangki = ""):
        self.__jnsMotor = jnsMotor
        self.__jmlTangki = jmlTangki
    
    #setter
    def setjnsMotor(self, jnsMotor):
        self.__jnsMotor = jnsMotor
    def setjmlTangki(self, jmlTangki):
        self.__jmlTangki = jmlTangki
     
    #getter
    def getjnsMotor(self):
        return self.__jnsMotor
    def getjmlTangki(self):
        return self.__jmlTangki
    