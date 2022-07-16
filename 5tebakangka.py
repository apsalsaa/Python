
for i in range (1):
    x=input("Silakan tebak angka! : ")
    
import random
angka = random.randrange(0, 10)

if int(x) == int(angka) :
    print("Selamat, tebakkan anda benar!")

elif int(x) > int(angka):
    print("Salah, Angka terlalu besar")
    
else:
    print("Salah, Angka terlalu kecil")