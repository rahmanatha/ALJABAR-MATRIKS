# NAMA : ABDU AR RAHMAN ATHALLAH
# NPM : 2515061002
# KELAS : PSTI D
# Modul untuk operasi matriks 3x3: penjumlahan, pengurangan, perkalian, dan transpose

def input_matriks(nama_matriks):
    matriks = []

    print("input nilai matriks", nama_matriks)

    for i in range(3):
        baris = []
        for j in range(3):
            nilai = int(input(f"masukkan nilai matriks {nama_matriks}[{i + 1}][{j + 1}]: "))
            baris.append(nilai)
        matriks.append(baris)

    return matriks


def tampilkan_matriks(matriks):
    for baris in matriks:
        print(baris)


def tambah_matriks(matriks_a, matriks_b):
    hasil = []

    for i in range(3):
        baris_baru = []
        for j in range(3):
            baris_baru.append(matriks_a[i][j] + matriks_b[i][j])
        hasil.append(baris_baru)

    return hasil


def kurang_matriks(matriks_a, matriks_b):
    hasil = []

    for i in range(3):
        baris_baru = []
        for j in range(3):
            baris_baru.append(matriks_a[i][j] - matriks_b[i][j])
        hasil.append(baris_baru)

    return hasil


def kali_matriks(matriks_a, matriks_b):
    hasil = []

    for i in range(3):
        baris_baru = []
        for j in range(3):
            total = 0
            for k in range(3):
                total = total + matriks_a[i][k] * matriks_b[k][j]
            baris_baru.append(total)
        hasil.append(baris_baru)

    return hasil


def transpose_matriks(matriks):
    hasil = []

    for i in range(3):
        baris_baru = []
        for j in range(3):
            baris_baru.append(matriks[j][i])
        hasil.append(baris_baru)

    return hasil