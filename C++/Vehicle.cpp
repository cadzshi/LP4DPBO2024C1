#pragma once
// library
#include <iostream>
#include <string>

using namespace std;

class Vehicle
{
    // atribut private
private:
    string plat;
    string merk;
    string tahun;
    string warna;

public:
    // constructor
    Vehicle()
    {
    }
    Vehicle(string plat, string merk, string tahun, string warna)
    {
        this->plat = plat;
        this->merk = merk;
        this->tahun = tahun;
        this->warna = warna;
    }

    // setter
    void setPlat(string plat)
    {
        this->plat = plat;
    }
    void setMerk(string merk)
    {
        this->merk = merk;
    }
    void setTahun(string tahun)
    {
        this->tahun = tahun;
    }
    void setWarna(string warna)
    {
        this->warna = warna;
    }

    // getter
    string getPlat()
    {
        return this->plat;
    }
    string getMerk()
    {
        return this->merk;
    }
    string getTahun()
    {
        return this->tahun;
    }
    string getWarna()
    {
        return this->warna;
    }

    // destructor
    ~Vehicle()
    {
    }
};