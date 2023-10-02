input_str = input("Введите список чисел через пробел: ")
A = input_str.split()
result = " ".join(A[::2])
print(result)