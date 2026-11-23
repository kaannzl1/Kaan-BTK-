öğrenciler = {}

for i in range(3):
    numara = input(f"{i + 1}. öğrencinin numarası: ")
    ad = input("Öğrencinin adı: ")
    soyad = input("Öğrencinin soyadı: ")
    telefon = input("Öğrencinin telefonu: ")

    öğrenciler[numara] = {
        "ad": ad,
        "soyad": soyad,
        "telefon": telefon,
    }

aranan_numara = input("Bilgilerini görmek istediğiniz öğrencinin numarası: ")
öğrenci = öğrenciler.get(aranan_numara)

if öğrenci:
    print(öğrenci)
else:
    print("Öğrenci bulunamadı")

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
