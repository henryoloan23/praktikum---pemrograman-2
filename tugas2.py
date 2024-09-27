import math

lintang1 = math.radians(float(input("Lintang Kota 1 = ")))
bujur1 = math.radians(float(input("Bujur Kota 1 = ")))
lintang2 = math.radians(float(input("Lintang kota 2 = ")))
bujur2 = math.radians(float(input("Bujur kota 2 = ")))

radius = 6371
lat = lintang2 - lintang1
long = bujur2 - bujur1

a =  math.sin(lat/2)*2 + math.cos(lintang1) * math.cos(lintang2) * math.sin(long/2)*2
C3 = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
d = radius * C3

print(f"jarak antara dua titik tersebut adalah ", (d) , "kilometer")






