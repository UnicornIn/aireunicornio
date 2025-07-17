# edad = int(input("Ingresa tu edad: "))
# if edad < 18:
#     print(f"Tienes {edad} años. Eres menor de edad.")
# elif edad < 60:
#     print(f"Tienes {edad} años. Eres un adulto.")
# else:
#     print(f"Tienes {edad} años. Eres una persona mayor.")


# x = int(input("Ingresa un número: "))
# if x % 3 == 0:
#     print(f"{x} es múltiplo de 3.")
# else:
#     print(f"{x} no es múltiplo de 3.")



# print("=== MENÚ PRINCIPAL ===")
# print("1. Saludar")
# print("2. Mostrar tabla del 9")
# print("3. Salir")

# # Leer opción del usuario
# opcion = input("Elige una opción (1-3): ")

# # Evaluar la opción
# if opcion == "1":
#     nombre = input("¿Cuál es tu nombre? ")
#     print(f"¡Hola, {nombre}!")
# elif opcion == "2":
#     print("Tabla del 9:")
#     for i in range(1, 11):
#         print(f"9 x {i} = {9 * i}")
# elif opcion == "3":
#     print("Saliendo del programa...")
# else:
#     print("Opción no válida.")

import random

# Generar un número secreto entre 1 y 10
numero_secreto = random.randint(1, 10)

print("¡Bienvenido al juego de adivinar el número secreto!")
print("Adivina un número del 1 al 10")

# Pedir al usuario que adivine
adivinanza = int(input("Tu número: "))

# Repetir hasta que adivine correctamente
while adivinanza != numero_secreto:
    if adivinanza < numero_secreto:
        print("Demasiado bajo. Intenta otra vez.")
    else:
        print("Demasiado alto. Intenta otra vez.")
    
    adivinanza = int(input("Tu número: "))

# Mensaje cuando acierta
print(f"¡Felicidades! Adivinaste el número secreto: {numero_secreto}")



    