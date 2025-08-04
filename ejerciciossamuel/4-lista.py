# 1. Crear una lista con 5 números e imprimirla
numeros = [1, 2, 3, 4, 5]
print(numeros)

#  Imprimir el primer y último elemento
print("Primero:", numeros[0])
print("Último:", numeros[-1])

#  Acceder a los elementos del índice 1 al 3
print(numeros[1:4])

# Cambiar el valor del segundo elemento
numeros[1] = 20
print(numeros)

#  Agregar un nuevo número al final
numeros.append(6)
print(numeros)

# 6. Recorrer una lista e imprimir cada elemento
for n in numeros:
    print(n)

#  Sumar todos los elementos de la lista
print("Suma:", sum(numeros))

#  Encontrar el mayor y menor valor
print("Máximo:", max(numeros))
print("Mínimo:", min(numeros))

#  Contar cuántas veces aparece un número
print("Veces que aparece 3:", numeros.count(3))

#  Verificar si un número está en la lista
print("¿Está el 4?", 4 in numeros)

#  Insertar un elemento en la posición 2
numeros.insert(2, 99)
print(numeros)

#  Eliminar un elemento por valor
numeros.remove(99)
print(numeros)

#  Eliminar el último elemento
numeros.pop()
print(numeros)

#  Ordenar la lista de menor a mayor
numeros.sort()
print(numeros)

#  Invertir el orden de la lista
numeros.reverse()
print(numeros)

#  Copiar una lista
copia = numeros.copy()
print("Copia:", copia)

#  Vaciar una lista
copia.clear()
print("Lista vacía:", copia)

#  Combinar dos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
combinada = lista1 + lista2
print("Combinada:", combinada)

# Crear una lista con los cuadrados del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print("Cuadrados:", cuadrados)

#  Filtrar elementos pares de una lista
numeros = [1, 2, 3, 4, 5, 6]
pares = [n for n in numeros if n % 2 == 0]
print("Pares:", pares)