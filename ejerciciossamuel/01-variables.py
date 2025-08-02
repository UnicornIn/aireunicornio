#es como un conjunto de reglas o normas que le permite a los programadores como interactuar con el computador

#variables 
edad = 78 #tipo int
nombre = "camilo" #tipo str se definine entree comillas simples o dobles 
#altura = 1.67 #tipo float que puede contener numeros desimales 
print("edad",edad,"nombre", nombre, ) 


numero1 = 165
numero2 = 67
suma = numero1 + numero2 
print(suma)



my_string_variable = "my string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str (my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#concatenacion de variables en un print 
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("este es el valor de mi :", my_bool_variable)

#algunas funcion del sistema 
print (len(my_string_variable))

#variables en una sola linea 
name, surname, alias, age = "andres", "gomez", "peque", 25
print("me llamo:", name, surname,". mi edad es:", age,". y mi alias es: " ,alias)

#inputs

name = input("¿cual es tu nombre? ")
age = input("¿cual es tu edad? ")
print(name)
print(age)

#cambiamos su tipo 
name = 35
age = 'andres'
print(name)
print(age)

#¿forzamos el tipo?    
address: str  = "mi direccion "
address = True
address = 5
address = 1.2
print(type(address))

llueve = False
if llueve: 
      print("llevo sombrilla")
else:  
      print("guardo la sombrilla")


llueve = 18 
print("18")


for i in range (7):
   print("samuel", i) 




# Pedir al usuario un número entero
N = int(input("Ingresa un número entero N: "))

# Inicializar la suma en 0
suma = 0

# Usar un ciclo for para sumar los primeros N números impares
for i in range(N):
    numero_impar = 2 * i + 1
    suma += numero_impar

# Imprimir el resultado
print("La suma de los primeros", N, "números impares es:", suma)

a=18
b=30

if a > b :
      print("es mayor ",a)
if b > a :

      print("es mayor ",b)

for i in range(1,   21):
    print(i)
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es PAR.")
else:
    print("El número es IMPAR.")
  