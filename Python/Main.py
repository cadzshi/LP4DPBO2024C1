#import library
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot
import os

#array
car = []
motorcycle = []
garage = []
parking = []

#set data
#car 
temp = Car()
temp.setplatNomor("L 9999 XY")
temp.setmerk("Lamborghini")
temp.settahunProduksi("2022")
temp.setwarna("Putih")
temp.setjmlKursi("2")
temp.setjmlPintu("2")
car.append(temp)

temp = Car()
temp.setplatNomor("R 0541 DD")
temp.setmerk("Mitsubishi")
temp.settahunProduksi("2021")
temp.setwarna("Ungu")
temp.setjmlKursi("6")
temp.setjmlPintu("4")
car.append(temp)

#motorcycle
temp = Motorcycle()
temp.setplatNomor("H 5678 AB")
temp.setmerk("Kawasaki")
temp.settahunProduksi("2023")
temp.setwarna("Hitam")
temp.setjnsMotor("Sport")
temp.setjmlTangki("17 Liter")
motorcycle.append(temp)

temp = Motorcycle()
temp.setplatNomor("B 8967 GG")
temp.setmerk("Scoppy")
temp.settahunProduksi("2000")
temp.setwarna("Pink")
temp.setjnsMotor("Scooter")
temp.setjmlTangki("8 Liter")
motorcycle.append(temp)

total = len(car) + len(motorcycle)

#garage
temp = Garage()
temp.setnamaGarasi("Jaya Garage")
temp.setluasGarasi("500 m2")
temp.setdaftarKendaraan("Mobil dan Motor")

temp1 = ParkingLot()
temp1.setkapasitas("10 Kendaraan")
temp1.setjmlKendaraan(total)
temp.setparking(temp1)

garage.append(temp)

#output
os.system('cls')
#data garasi
if not garage:
    print("Data Garasi Masih Kosong!")
else:
    print("+======================================+")
    print("|              Data Garasi             |")
    print("+======================================+")

    for Garage in garage:
        print("Nama Garasi      :", Garage.getnamaGarasi())
        print("Luas Garasi      :", Garage.getluasGarasi())
        print("Daftar Kendaraan :", Garage.getdaftarKendaraan())
        for parking in Garage.getparking():
            print("Total Kapasitas  :",parking.getkapasitas())
            print("Jumlah Saat Ini  :",parking.getjmlKendaraan(), "Kendaraan")

    print("========================================")
    
#data mobil
if not car:
    print("Data Mobil Masih Kosong!")
else:
    i = 1
    print("Data Mobil :")
    for Car in car:
        print(i, end=". ")
        print("Nomor Plat       :", Car.getplatNomor())
        print("   Merk             :", Car.getmerk())
        print("   Tahun Produksi   :", Car.gettahunProduksi())
        print("   Warna            :", Car.getwarna())
        print("   Jumlah Kursi     :", Car.getjmlKursi())
        print("   Jumlah Pintu     :", Car.getjmlPintu())
        i += 1
        print("========================================")

print("")
#data motor 
if not motorcycle:
    print("Data Motor Masih Kosong!")
else:
    i = 1
    print("Data Motor :")
    for Motorcycle in motorcycle:
        print(i, end=". ")
        print("Nomor Plat           :", Motorcycle.getplatNomor())
        print("   Merk                 :", Motorcycle.getmerk())
        print("   Tahun Produksi       :", Motorcycle.gettahunProduksi())
        print("   Warna                :", Motorcycle.getwarna())
        print("   Jenis Motor          :", Motorcycle.getjnsMotor())
        print("   Kapasitas Tangki     :", Motorcycle.getjmlTangki())
        i += 1
        print("========================================")




