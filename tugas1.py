import math
nilai1 = float(input('masukkan nilai A = '))
nilai2 = float(input('masukkan nilai B = '))

penjumlahan = nilai1 + nilai2
print(f'hasil dari penjumlahan A + B adalah {float(penjumlahan)}')

selisih = nilai1 - nilai2
print(f'selisih antara nilai A dan B adalah {float(selisih)}')

perkalian = nilai1 * nilai2
print(f'jumlah A dikali B adalah {float(perkalian)}')

pembagian = nilai1 / nilai2
print(f'jumlah A di bagi B adalah {float(pembagian)}')

modulus = nilai1 % nilai2
print(f'jumlah sisa pembagian dari A dan B adalah {float(modulus)}')

pangkat = nilai1 ** nilai2
print(f'hasil A dipangkat B adalah {float(pangkat)}')

logA = math.log(nilai1)
print(f'hasil dari log A adalah {float(logA)}')