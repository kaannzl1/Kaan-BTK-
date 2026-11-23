# 1- Girilen sayının 0-100 arasında olup olmadığını kontrol et

sayi = float(input("sayı: "))
result = (sayi > 0) and (sayi <= 100)
if result:
    print("sayı 0-100 arasında.")
else:
    print("sayı 0-100 arasında değildir.")
