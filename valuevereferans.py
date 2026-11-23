# value type reference
x = 5
y = 25
x = y
y = 10
# print(x + y)


# reference types => list
a = ["apple", "banana", "kiwi"]
b = ["apple", "banana", "kiwi"]
a = b
b[0] = "orange"
print(a, b)
