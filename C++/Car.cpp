#pragma once

#include <iostream>
#include <string.h>
#include "Vehicle.cpp"

using namespace std;

class Car : public Vehicle
{
    // atribut private
private:
    string kursi;
    string pintu;

public:
    // constructor
    Car()
    {
    }
    Car(string kursi, string pintu, string nomor, string merk, string tahun, string warna) : Vehicle(nomor, merk, tahun, warna)
    {
        this->kursi = kursi;
        this->pintu = pintu;
    }

    // setter
    void setKursi(string kursi)
    {
        this->kursi = kursi;
    }
    void setPintu(string pintu)
    {
        this->pintu = pintu;
    }

    // getter
    string getKursi()
    {
        return this->kursi;
    }
    string getPintu()
    {
        return this->pintu;
    }

    ~Car()
    {
    }
};