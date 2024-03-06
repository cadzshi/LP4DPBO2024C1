#pragma once

#include <iostream>
#include <string.h>
#include "Vehicle.cpp"

using namespace std;

class Motorcycle : public Vehicle
{
    // atribut private
private:
    string jenis;
    string tangki;

public:
    // constructor
    Motorcycle()
    {
    }
    Motorcycle(string jenis, string tangki, string nomor, string merk, string tahun, string warna) : Vehicle(nomor, merk, tahun, warna)
    {
        this->jenis = jenis;
        this->tangki = tangki;
    }

    // setter
    void setJenis(string jenis)
    {
        this->jenis = jenis;
    }
    void setTangki(string tangki)
    {
        this->tangki = tangki;
    }

    // getter
    string getJenis()
    {
        return this->jenis;
    }
    string getTangki()
    {
        return this->tangki;
    }

    ~Motorcycle()
    {
    }
};