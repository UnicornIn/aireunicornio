#  Suma de dos números
a = 5
b = 7
print("Suma:", a + b)

#  Área de un triángulo
base = 10
altura = 6
area = (base * altura) / 2
print("Área del triángulo:", area)

#  Cuadrado y raíz cuadrada de un número
n = 9
print("Cuadrado:", n ** 2)
print("Raíz cuadrada:", n ** 0.5)

#  Módulo entre dos números
x = 17
y = 5
print("Módulo:", x % y)

#  Conversión de Celsius a Fahrenheit
c = 30
f = c * 1.8 + 32
print("Fahrenheit:", f)

#  Verifica si un número es mayor que otro
x = 10
y = 8
print("¿x > y?", x > y)

#  Determina si un número es par
n = 12
print("¿Es par?", n % 2 == 0)

#  ¿Quién es mayor?
edad1 = 25
edad2 = 30
print("Persona 2 es mayor:", edad2 > edad1)

#  ¿Número entre 1 y 100?
num = 77
print("¿Está entre 1 y 100?", 1 <= num <= 100)

#  ¿Son dos números iguales?
a = 5
b = 5
print("¿Son iguales?", a == b)

#  ¿Número entre 10 y 50 y es par?
n = 24
print("¿Entre 10 y 50 y par?", n >= 10 and n <= 50 and n % 2 == 0)

#  Acceso a sistema
activo = True
admin = False
print("¿Acceso?", activo or admin)

#  ¿Número NO entre 20 y 40?
n = 18
print("¿Fuera del rango 20-40?", not (20 <= n <= 40))

#  Diferentes y mayores que 5
a = 6
b = 8
print("¿Diferentes y >5?", a != b and a > 5 and b > 5)

#  Validar usuario y contraseña
usuario = "admin"
clave = "1234"
print("¿Acceso permitido?", usuario == "admin" and clave == "1234")

#  Acumulando suma del 1 al 10
suma = 0
for i in range(1, 11):
    suma += i
print("Suma 1 al 10:", suma)

#  Multiplicar usando *=
valor = 4
valor *= 3
print("Valor duplicado:", valor)

#  Resta con -=
n = 100
n -= 5
print("Nuevo valor:", n)

#  Modificar variable paso a paso
x = 10
x //= 3  # División entera
x %= 4   # Módulo
x **= 2  # Potencia
print("Resultado final:", x)

#  Uso de 'in' y 'is'
lista = [1, 2, 3, 4]
a = 2
b = 2
print("¿2 está en la lista?", a in lista)
print("¿a es b?", a is b)