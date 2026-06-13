# NAMA : ABDU AR RAHMAN ATHALLAH
# NPM : 2515061002
# KELAS : PSTI D
# Main Program untuk modul operasi matriks 3x3: penjumlahan, pengurangan, perkalian, dan transpose

import atha002 as at

print("Program DiKhususkan untuk Operasi Matriks 3x3")
print("===========================")

print("\nMatriks a")
matriks_a = at.input_matriks("a")

print("\nMatriks b")
matriks_b = at.input_matriks("b")


print("\nmatriks a:")
at.tampilkan_matriks(matriks_a)

print("\nmatriks b:")
at.tampilkan_matriks(matriks_b)


print("\nhasil penjumlahan matriks a + b:")
hasil_tambah = at.tambah_matriks(matriks_a, matriks_b)
at.tampilkan_matriks(hasil_tambah)


print("\nhasil pengurangan matriks a - b:")
hasil_kurang = at.kurang_matriks(matriks_a, matriks_b)
at.tampilkan_matriks(hasil_kurang)


print("\nhasil perkalian matriks a x b:")
hasil_kali = at.kali_matriks(matriks_a, matriks_b)
at.tampilkan_matriks(hasil_kali)


print("\ntranspose matriks a:")
hasil_transpose_a = at.transpose_matriks(matriks_a)
at.tampilkan_matriks(hasil_transpose_a)


print("\ntranspose matriks b:")
hasil_transpose_b = at.transpose_matriks(matriks_b)
at.tampilkan_matriks(hasil_transpose_b)