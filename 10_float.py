x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

#Forma brusca (Strings)
y_str = format(y, ".2g")
print("str =>", y_str)
print(y_str == str(x))

print('*' * 20)

#Forma matemática
print(y, x)
tolerance = 0.00001
print(abs(x - y) < tolerance)