#  Crear una tupla con 5 elementos
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)

#  Imprimir el primer y último elemento
print("Primero:", mi_tupla[0])
print("Último:", mi_tupla[-1])

#  Acceder a los elementos del índice 1 al 3
print("Subtupla:", mi_tupla[1:4])

#  Verificar si un elemento está en la tupla
print("¿Está el 3?", 3 in mi_tupla)

#  Intentar cambiar un valor (esto generará un error)
try:
    mi_tupla[0] = 10
except TypeError as e:
    print("Error:", e)

#  Obtener la longitud de la tupla
print("Longitud:", len(mi_tupla))

#  Contar cuántas veces aparece un número
print("Veces que aparece 2:", mi_tupla.count(2))

#  Obtener el índice de un valor
print("Índice del 4:", mi_tupla.index(4))

#  Recorrer la tupla con un bucle
for valor in mi_tupla:
    print(valor)

#  Usar tuplas en una estructura condicional
if 4 in mi_tupla:
    print("El número 4 está en la tupla")

#  Convertir tupla a lista
lista = list(mi_tupla)
print("Como lista:", lista)

#  Convertir lista a tupla
nueva_tupla = tuple(lista)
print("Como tupla:", nueva_tupla)

#  Concatenar dos tuplas
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print("Concatenada:", t3)

#  Repetir una tupla
repetida = t1 * 3
print("Repetida:", repetida)

#. Comparar dos tuplas
print("¿t1 == t2?", t1 == t2)

#  Crear una tupla con diferentes tipos de datos
mixta = ("texto", 123, True, 3.14)
print("Tupla mixta:", mixta)

#  Crear una tupla de una sola posición
una_sola = (7,)
print("Tupla de un solo elemento:", una_sola)

#. Desempaquetar una tupla en variables
tupla = (10, 20, 30)
a, b, c = tupla
print(f"a={a}, b={b}, c={c}")

#  Usar tupla como clave de un diccionario
coordenada = (3, 4)
dic = {coordenada: "Punto A"}
print(dic)

#  Iterar con índice usando enumerate
for i, valor in enumerate(mi_tupla):
    print(f"Índice {i}: {valor}")
