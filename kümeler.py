fruits = {"elma", "armut", "muz"}
# print(fruits) indexlenemezler

for fruit in fruits:
    print(fruit)

fruits.update(["karpuz", "kavun"])
fruits.add("çilek")
print(fruits)

fruits.remove("armut")
fruits.discard("elma")  # silmek istediğimiz eleman yoksa hata vermez
fruits.clear()  # tüm elemanları siler


# myList = [1, 2, 5, 4, 4, 2]
# mySet = set(myList)  #tekrar eden elemanları siler
# print(mySet)
