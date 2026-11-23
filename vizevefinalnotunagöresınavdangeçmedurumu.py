# 1- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız

vize1 = float(input("1. vize: "))
vize2 = float(input("2. vize: "))
final = float(input("final: "))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

print(f"not ortalamanız : {ortalama} ve dersten geçme durumunuz : {ortalama >= 50}")
