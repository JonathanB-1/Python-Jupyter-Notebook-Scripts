def fib(n):
    a = 0
    b = 1

    for _ in range (n):
        c = a+b
        a = b
        b = c
    return b

for x in range(int(input("Por favor ingrese el número de la sucesión que desea calcular: "))):

    print(fib(x))

print(" ")
print("El número de la sucesión es el siguiente: ")
print(" ")
print(fib(x))