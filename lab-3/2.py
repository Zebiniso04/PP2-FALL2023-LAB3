input_str = input("Введите список чисел через пробел: ")
A = input_str.split()
result = " ".join([x for x in A if int(x) % 2 == 0])
print(result)