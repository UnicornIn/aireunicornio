# edad = int(input("Ingresa tu edad: "))
# if edad < 18:
#     print("Eres menor de edad.")
# elif edad < 70:
#     print("Eres mayor de edad.")
# else:
#     print("Eres adulto mayor.")

# #

# numero = int(input("introduce un numero:"))
# if numero % 3 == 0:
#     print(f"{numero} es multiplo de 3")
# else:
#     print(f"{numero} no es multiplo de 3")

# #

# print("=== MENU PRINCIPAL ===")
# print("1. Saludar")
# print("2. sumar dos numeros")
# print("3. salir")
# opcion = int(input("elige una opcion:"))

# if opcion == 1:
#     nombre = input("cual es tu nombre?:")
#     print(f"Hola {nombre}!")
# elif opcion == 2:
#     num1 = int(input("introduce el primer numero:"))
#     num2 = int(input("introduce el segundo numero:"))
#     print(f"La suma es: {num1 + num2}")
# elif opcion == 3:
#     print("Saliendo...¡adiós!")
# else:
#     print("Opcion no valida; por favor eliga un numero del 1 al 3.")

#     #

import random

Secreto = random.randint(1, 10)
intentos = 0

while intentos < 3:
    numero = int(input("Adivina el numero entre 1 y 10: "))
    if numero == Secreto:
        print("¡Felicidades! Adivinaste el numero.")
        break
    else:
        print("Intenta de nuevo.")
    intentos += 1

if intentos == 3:
    print(f"Lo siento, el numero secreto era {Secreto}.")