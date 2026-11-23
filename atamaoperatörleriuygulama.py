x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x, y ve z toplamının farkı nedir?

a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz: "))
result = (a * b) - (x + y + z)
print("Sonuç: ", result)

# 2- y'nin x'e kalansız bölümünü hesaplayınız.

result2 = y // x
print("y'nin x'e kalansız bölümü: ", result2)

# 3- (x,y,z) toplamının mod 3'ü nedir?

result3 = (x + y + z) % 3
print("(x, y, z) toplamının mod 3'ü: ", result3)

# 4- y'nin x. kuvvetini hesaplayınız.

result4 = y**x
print("y'nin x. kuvveti: ", result4)

# 5- x, *y, z = numbers işlemine göre z'nin küpü nedir?

x, *y, z = numbers
result5 = z**3
print("z'nin küpü: ", result5)

# 6- x, *y, z = numbers işemine göre y nin değerleri toplamı kaçtır?

x, *y, z = numbers
result6 = sum(y)
print("y'nin değerleri toplamı: ", result6)
