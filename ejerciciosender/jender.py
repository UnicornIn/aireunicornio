#numero = int(input("introduce un numero entero: "))

#f numero % 3 == 0:
   # print("El numero es multiplo de 3")
#else: 
  #  print("El numero no es multiplo de 3")

# print("1. verifica si un numero es par o impar")
# print("2 carcula el cuadrado de un numero")
# print("3.mostrar los primeros 5 multiplo de un numero ")
# print("4. salir")

# opcion = input("elige una opcion (1-4): ")

# if opcion == "1":
#     numero = int(input("introduce un numero entero: "))
#     if numero % 2 == 0:
#         print("El numero es par")
#     else:
#         print("El numero es impar")

# elif opcion == "2":
#     numero = float(input("introduce un numero entero: "))
#     print("El cuadrado de", numero, "es", numero ** 2) 

# elif opcion == "3":
#     numero = int(input("introduce un numero entero: "))
#     print("Los primeros 5 multiplos de", numero, "son:")
#     for i in range(1, 6):
#         print(numero * i)

# elif opcion == "4":
#     print("Saliendo del programa...")


# else:
#     print("Opción no válida. Por favor, elige una opción entre 1 y 4.")

import random

numero_secreto = random.randint(1, 10)

print("Adivina el número secreto entre 1 y 10")

while True:
    intento = int(input("Ingresa un número: "))

    if intento < numero_secreto:
        print("Muy bajo, intenta de nuevo.")
    elif intento > numero_secreto:
        print("Muy alto, intenta de nuevo.")
    else:
        print("¡Felicidades! Adivinaste el número secreto:", numero_secreto)
        break  # Sale del bucle cuando adivina
