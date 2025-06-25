# pide al usuari una palabra 
palabra = input("reconocer")

#convierte la palabra a mayusculas
palabra = palabra.lower()

# invierte la palabra 
palabra_invertida = palabra[::-1]

# compara la palabra originales con la invertida 
if palabra == palabra_invertida:
    print("la palabra es palindromo")
else:
    print("la palabra no es palindromo")