#pragma once
// library
#include <iostream>
#include <string.h>

using namespace std;

class Garage
{
    // atribut private
private:
    string nama;
    string luas;
    string daftar;

public:
    // constructor
    Garage()
    {
    }
    Garage(string nama, string luas, string daftar)
    {
        this->nama = nama;
        this->luas = luas;
        this->daftar = daftar;
    }

    // setter
    void setNama(string nama)
    {
        this->nama = nama;
    }
    void setLuas(string luas)
    {
        this->luas = luas;
    }
    void setDaftar(string daftar)
    {
        this->daftar = daftar;
    }

    // getter
    string getNama()
    {
        return this->nama;
    }
    string getLuas()
    {
        return this->luas;
    }
    string getDaftar()
    {
        return this->daftar;
    }

    // destructor
    ~Garage()
    {
    }
};