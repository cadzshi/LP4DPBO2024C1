// library
#include <bits/stdc++.h>
#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"
#include "Garage.cpp"

using namespace std;

int main()
{
    Garage garage("Jaya Garage", "500 m2", "Mobil dan Motor");

    cout << "+======================================+" << endl;
    cout << "|              Data Garasi             |" << endl;
    cout << "+======================================+" << endl;
    cout << "Nama Garasi      : " << garage.getNama() << endl;
    cout << "Luas Garasi      : " << garage.getLuas() << endl;
    cout << "Daftar Kendaraan : " << garage.getDaftar() << endl;
    cout << "========================================" << endl;

    // instansiasi
    Car car("2", "2", "L 9999 XY", "Lamborghini", "2022", "Putih");
    // ouput data mobil
    cout << "Data Mobil : " << endl;
    cout << "Nomor Plat     : " << car.getPlat() << endl;
    cout << "Merk           : " << car.getMerk() << endl;
    cout << "Tahun Produksi : " << car.getTahun() << endl;
    cout << "Warna          : " << car.getWarna() << endl;
    cout << "Jumlah Kursi   : " << car.getKursi() << endl;
    cout << "Jumlah Pintu   : " << car.getPintu() << endl;
    cout << "========================================" << endl;

    // instansiasi
    Motorcycle motor("Sport", "17 Liter", "H 7686 GB", "Kawasaki", "2023", "Ungu");
    // ouput data mobil
    cout << "Data Motor : " << endl;
    cout << "Nomor Plat         : " << motor.getPlat() << endl;
    cout << "Merk               : " << motor.getMerk() << endl;
    cout << "Tahun Produksi     : " << motor.getTahun() << endl;
    cout << "Warna              : " << motor.getWarna() << endl;
    cout << "Jenis Motor        : " << motor.getJenis() << endl;
    cout << "Kapasitas Tangki   : " << motor.getTangki() << endl;
    cout << "========================================" << endl;

    return 0;
}