#  Crear un diccionario con información de una persona
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Lima"}
print(persona)

#  Acceder al valor de una clave
print("Nombre:", persona["nombre"])

#  Modificar el valor de una clave
persona["edad"] = 26
print("Edad actualizada:", persona["edad"])

#  Agregar una nueva clave
persona["profesion"] = "Ingeniera"
print(persona)

#  Eliminar una clave con `del`
del persona["ciudad"]
print(persona)

#  Usar .get() para obtener un valor sin error
print("Correo:", persona.get("correo", "No disponible"))

#  Obtener todas las claves con .keys()
print("Claves:", persona.keys())

#  Obtener todos los valores con .values()
print("Valores:", persona.values())

#  Obtener todos los pares clave-valor con .items()
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

#  Verificar si una clave existe
print("¿Existe 'nombre'?", "nombre" in persona)

#  Recorrer solo las claves
for clave in persona:
    print(clave)

#  Contar cuántos elementos tiene el diccionario
print("Cantidad de elementos:", len(persona))

#  Vaciar el diccionario
persona.clear()
print("Diccionario vacío:", persona)

#  Copiar un diccionario
persona = {"nombre": "Ana", "edad": 25}
copia = persona.copy()
print("Copia:", copia)

#  Eliminar una clave con pop()
edad = persona.pop("edad")
print("Edad eliminada:", edad)
print(persona)

#  Crear diccionario a partir de dos listas
claves = ["a", "b", "c"]
valores = [1, 2, 3]
dic = dict(zip(claves, valores))
print(dic)

#  Contar letras en una palabra
palabra = "banana"
contador = {}
for letra in palabra:
    contador[letra] = contador.get(letra, 0) + 1
print("Conteo:", contador)

#  Crear diccionario con valores predeterminados
nombres = ["Luis", "Ana", "Pedro"]
notas = dict.fromkeys(nombres, 0)
print(notas)

#  Diccionario con listas como valores
estudiantes = {
    "Ana": [18, 20, 19],
    "Luis": [15, 16, 14]
}
print("Notas de Ana:", estudiantes["Ana"])

#  Sumar todos los valores del diccionario
ventas = {"enero": 100, "febrero": 150, "marzo": 120}
print("Ventas totales:", sum(ventas.values()))