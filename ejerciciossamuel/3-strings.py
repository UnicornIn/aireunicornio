#  Concatenar dos cadenas
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

#  Longitud de una cadena
texto = "Hola mundo"
print("Longitud:", len(texto))

#  Convertir a mayúsculas y minúsculas
frase = "Python es divertido"
print(frase.upper())
print(frase.lower())

#  Repetir una cadena 3 veces
palabra = "¡Hola! "
print(palabra * 3)

#  Extraer el primer y último carácter
s = "programación"
print("Primero:", s[0])
print("Último:", s[-1])

#  Obtener los primeros 5 caracteres
mensaje = "Bienvenidos"
print(mensaje[:5])

# Invertir una cadena
cadena = "Python"
print(cadena[::-1])

#  Formateo con f-string
nombre = "Ana"
edad = 28
print(f"{nombre} tiene {edad} años.")

# Reemplazar texto en una cadena
texto = "Me gusta Java"
nuevo_texto = texto.replace("Java", "Python")
print(nuevo_texto)

#  Contar cuántas veces aparece una letra
frase = "banana"
print("Veces que aparece 'a':", frase.count("a"))

#  Verificar si una cadena comienza con un prefijo
palabra = "computadora"
print(palabra.startswith("com"))

#  Verificar si termina con cierto sufijo
archivo = "foto.png"
print(archivo.endswith(".png"))

#  Quitar espacios al inicio y final
espaciado = "  hola mundo  "
print(espaciado.strip())

#  Convertir a lista de palabras
oracion = "Python es poderoso"
palabras = oracion.split()
print(palabras)

#  Unir palabras con guiones
palabras = ["uno", "dos", "tres"]
frase = "-".join(palabras)
print(frase)

#  Comprobar si un string contiene solo letras
nombre = "Carlos"
print(nombre.isalpha())

#  Comprobar si un string contiene solo números
numero = "123456"
print(numero.isdigit())

#  Verificar si una palabra está en una frase
frase = "El lenguaje Python es excelente"
print("Python" in frase)

#  Comparar dos cadenas ignorando mayúsculas/minúsculas
a = "Python"
b = "python"
print(a.lower() == b.lower())

#  Reemplazar múltiples espacios por uno solo
import re
texto = "Hola     mundo    Python"
limpio = re.sub(r'\s+', ' ', texto)
print(limpio)