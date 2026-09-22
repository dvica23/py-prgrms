a, b = 33, 44
temp = a
a = b
b = temp
print("Using Temp:", a, b)

a, b = 33, 44
a, b = b, a
print("Using ,:", a, b)

a, b = 33, 44
a = a + b
b = a - b
a = a - b
print("Using + & -:", a, b)

a, b = 33, 44
a = a ^ b
b = a ^ b
a = a ^ b
print("Using ^:", a, b)
