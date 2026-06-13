# Operasi Matriks 3x3 Menggunakan Module Python

## Identitas

**Nama:** Abdu Ar Rahman Athallah
**NPM:** 2515061002
**Kelas:** PSTI D

## Deskripsi Project

Project ini dibuat untuk memenuhi tugas Ujian Akhir Semester mata kuliah Struktur Data. Program ini menggunakan konsep **module/library Python** untuk melakukan operasi matriks 3x3.

File utama dalam project ini terdiri dari:

* `atha002.py` sebagai module yang berisi fungsi-fungsi operasi matriks.
* `main.py` sebagai program utama untuk mengimport dan menjalankan fungsi dari module.

Program ini dapat melakukan beberapa operasi matriks, yaitu:

1. Input matriks 3x3 dari user
2. Menampilkan matriks
3. Penjumlahan matriks
4. Pengurangan matriks
5. Perkalian matriks
6. Transpose matriks

## Struktur File

```text
project_matriks/
│
├── atha002.py
├── main.py
└── README.md
```

## Penjelasan File

### 1. atha002.py

File `atha002.py` merupakan module Python yang berisi beberapa fungsi untuk operasi matriks 3x3.

Fungsi yang terdapat pada module ini adalah:

| Nama Fungsi                            | Kegunaan                                             |
| -------------------------------------- | ---------------------------------------------------- |
| `input_matriks(nama_matriks)`          | Meminta input nilai matriks 3x3 dari user            |
| `tampilkan_matriks(matriks)`           | Menampilkan isi matriks ke layar                     |
| `tambah_matriks(matriks_a, matriks_b)` | Menjumlahkan dua matriks 3x3                         |
| `kurang_matriks(matriks_a, matriks_b)` | Mengurangkan dua matriks 3x3                         |
| `kali_matriks(matriks_a, matriks_b)`   | Mengalikan dua matriks 3x3                           |
| `transpose_matriks(matriks)`           | Mengubah baris menjadi kolom dan kolom menjadi baris |

### 2. main.py

File `main.py` merupakan program utama. File ini digunakan untuk menjalankan program dengan cara mengimport module `atha002.py`.

Pada file `main.py`, module diimport menggunakan kode berikut:

```python
import atha002 as at
```

Penggunaan `as at` berfungsi sebagai alias, sehingga pemanggilan fungsi menjadi lebih singkat.

Contoh:

```python
matriks_a = at.input_matriks("a")
```

## Cara Menjalankan Program

1. Pastikan file `atha002.py` dan `main.py` berada dalam folder yang sama.
2. Buka terminal atau Command Prompt pada folder tersebut.
3. Jalankan program utama dengan perintah:

```bash
python main.py
```

Atau jika menggunakan Python 3:

```bash
python3 main.py
```

## Alur Program

1. Program mengimport module `atha002.py`.
2. User diminta memasukkan nilai matriks A berukuran 3x3.
3. User diminta memasukkan nilai matriks B berukuran 3x3.
4. Program menampilkan matriks A dan matriks B.
5. Program menghitung dan menampilkan hasil:

   * Penjumlahan matriks A dan B
   * Pengurangan matriks A dan B
   * Perkalian matriks A dan B
   * Transpose matriks A
   * Transpose matriks B

## Contoh Input

Contoh input matriks A:

```text
1 2 3
4 5 6
7 8 9
```

Contoh input matriks B:

```text
9 8 7
6 5 4
3 2 1
```

## Konsep yang Digunakan

Project ini menggunakan beberapa konsep dasar Python, yaitu:

* Module
* Fungsi
* Parameter
* List
* Nested list
* Perulangan `for`
* Input user
* Operasi aritmatika
* Return value

## Kesimpulan

Dengan menggunakan module, program menjadi lebih rapi dan terstruktur. File `atha002.py` berisi kumpulan fungsi operasi matriks, sedangkan file `main.py` digunakan sebagai program utama untuk memanggil dan menjalankan fungsi-fungsi tersebut.
