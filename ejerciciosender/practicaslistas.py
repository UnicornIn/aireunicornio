# animales = ["gato", "perro", "conejo", "tigre"]

# for animal in animales:
#     print(animal)


# frutas = ["manzana", "pera", "uva"]
# frutas.append("naranja")

# print(frutas)


# numeros = [4, 7, 2, 9]
# suma = sum(numeros)

# print("La suma es:", suma)


# numero = 1

# while numero <= 5:
#     print(numero)
#     numero = numero + 1  

# for numero in range(1, 6):
#     print(numero, end=" ")


# numeros = [5, 8, 3, 2, 7]

# suma = 0

# for numero in numeros:
#     suma += numero 


# def sumar_dos_numeros():
#     numero1 = float(input("Ingresa el primer número: "))
#     numero2 = float(input("Ingresa el segundo número: "))
#     suma = numero1 + numero2
#     return suma

# # Llamamos a la función y mostramos el resultado
# resultado = sumar_dos_numeros()
# print("La suma es:", resultado)

# # Pedir al usuario un número
# numero = int(input("Introduce un número: "))

# # Verificar si es par o impar
# if numero % 2 == 0:
#     print("El número es par.")
# else:
#     print("El número es impar.")

# edad = int(input("¿Cuántos años tienes? "))

# if edad >= 18:
#     print("Eres mayor de edad.")
# else:
#     print("No eres mayor de edad.")

# def puede_votar(edad):
#     if edad >= 18:
#         print("Puede votar")
#     else:
#         print("No puede votar")

# # Ejemplo de uso
# edad_usuario = int(input("Ingresa tu edad: "))
# puede_votar(edad_usuario)



def saludar(nombre):
     print("¡Hola,", nombre + "!")
#ejemplo de uso 
saludar("ender")