n =int(input("introduce un numero entero n: "))

suma = 0
for i in range(n):
    numero_impar = 2 * i + 1
    suma += numero_impar

print("La suma de los primeros", n, "números impares es:", suma)