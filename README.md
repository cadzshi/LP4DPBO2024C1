# LP4DPBO2024C1

## Janji

Saya Sabila Rosad NIM 2106000 mengerjakan latihan 4
dalam mata kuliah Desain Pemrograman Berorientasi Objek
untuk keberkahanNya maka saya tidak melakukan
kecurangan seperti yang telah dispesifikasikan
Aamiin.

## Soal

Buatlah program berbasis OOP menggunakan bahasa pemrograman C++ dan Python yang mengimplementasikan konsep inheritance, composition, dan array of object pada kelas-kelas berikut :

- Vehicle : plat nomor, merk, tahun produksi, warna
- Car : jumlah kursi, jumlah pintu
- Motorcycle : jenis motor, kapasitas tangki
- Garage : nama garasi, luas garasi, daftar kendaraan
- ParkingLot : kapasitas, jumlah kendaraan saat ini

## Desain Program

![image](https://media.discordapp.net/attachments/957671708058325032/1214909668883828746/image.png?ex=65fad3cc&is=65e85ecc&hm=d7e2a1e51f0432c91152ca1a9193df608133a111d847a5525a8793dd1acd011b&=&format=webp&quality=lossless&width=526&height=671) <br>
Alasan desain program : <br>
a. Car dan Motorcycle is a Vehicle, Vehicle menjadi kelas parent, sedangkan Car dan Motorcycle menjadi kelas child
b. Car dan Motorcycle has a Garage
c. Garage has a ParkingLot

A. Class Vehicle

- Atribut :
  - plat : nomor plat dari kendaraan
  - merk : merk dari kendaraan
  - tahunProduksi : tahun berapa kendaraan itu diproduksi
  - warna : warna dari kendaraan
- Methods :
  - set() : menetapkan nilai sebuah value
  - get() : mendapatkan nilai sebuah value

B. Class Car

- Atribut :
  - jmlkursi : jumlah kursi sebuah mobil
  - jmlpintu : jumlah pintu sebuah mobil
- Methods :
  - set() : menetapkan nilai sebuah value
  - get() : mendapatkan nilai sebuah value

C. Class Motorcycle

- Atribut :
  - jnsmotor : jenis dari sebuah motor
  - kapasitas : kapasitas tangki
- Methods :
  - set() : menetapkan nilai sebuah value
  - get() : mendapatkan nilai sebuah value

D. Class Garage

- Atribut
  - nama : nama garasi
  - luas : luas garasi
  - daftar : daftar kendaraan yang ada di garasi
- Methods :
  - set() : menetapkan nilai sebuah value
  - get() : mendapatkan nilai sebuah value

E. Class ParkingLot

- Atribut :
  - kapasitas : kapasitas sebuah parkinglot
  - jumlahSekarang : jumlah kendaraan yang ada sekarang
- Methods :
  - set() : menetapkan nilai sebuah value
  - get() : mendapatkan nilai sebuah value

## Dokumentasi dan Alur Program

Untuk dokumentasi menggunakan screenshot yang sudah tersedia di masing-masing folder bahasa.

Lalu untuk alur program : <br>

1. Compile file sesuai bahasa
2. Run programnya
3. Ketika program berhasil dijalankan, maka akan menampilkan data sebuah garasi, dan data kendaraan (mobil dan motor)
4. Data yang ada merupakan Hardcoded
