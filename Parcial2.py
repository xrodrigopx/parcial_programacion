text = "X-DSPAM-Confidence:    0.8475"

find_number = text.find("0")
number = (text[text.find("0"):])
fl_number = float(number)
print (fl_number)

#######################################################

arch1 = open ("C:\Python\ej2-archivo1.txt")
for line in arch1:
    line = line.rstrip()
    if line.startswith("From: "):
        print(line)

arch1 = open ("C:\Python\ej2-archivo1.txt")
for line in arch1:
    line = line.rstrip()
    if not line.startswith("From: "):
        continue
    print(line)

#pide al usuario el nombre del archivo 
fname = input ("Enter file name: ")
fhand = open (fname) #abre el archivo
count = 0 #contador para las líneas
for line in fhand:
    if line.startswith("Subjetct:"): #loop para discriminar cuales lineas
        count +=1 #aumenta el contador
print ("There were", count, "subject lines in", fname) #imprime lo que buscamos


#pide al usuario el nombre del archivo 
fname = input ("Enter file name: ")
try: #ah shit... here we go again
    fhand = open (fname) #abre el archivo, o debería
except: #por si explota
    print("meh, wrong file name: ", fname)
    quit()

count = 0 #contador para las líneas
for line in fhand:
    if line.startswith("Subjetct:"): #loop para discriminar cuales lineas
        count +=1 #aumenta el contador
print ("There were", count, "subject lines in", fname) #imprime lo que buscamos


# devuelve un texto completo en mayusculas
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
for lines in inp:
    line = lines.strip()
print(inp.upper())

##########################################################
count = 0
total = 0.0

file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                count += 1
                value = float(line.split(':')[1])
                total += value

    if count > 0:
        average = total / count
        print("Average spam confidence: {}".format(average))
    else:
        print("No lines with the specified format were found.")
except FileNotFoundError:
    print("File not found.")

######################################
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line.rstrip())
print("Done")

"""1. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dolar':'us$', 'Yen':'¥', 'Peso':'$', 'Real':'R$'}, luego pregunte al usuario por una divisa y muestre su símbolo (o un mensaje de aviso si la divisa no está en el diccionario). 
"""
divisas = {'Euro':'€', 'Dolar':'us$', 'Yen':'¥', 'Peso':'$', 'Real':'R$'}
divisa = input("Ingrese una divisa: ")

if divisa in divisas:
    simbolo = divisas[divisa]
    print(f"El símbolo de {divisa} es {simbolo}")
else:
    print("La divisa no está en el diccionario.")

"""2. Escribir un programa que almacene el diccionario con los créditos de las asignaturas de una carrera {'Matemáticas': 6, 'Física': 4, 'Química': 5, 'Contabilidad': 8, 'Programación: 6, 'Redacción': 6, 'Trabajo final': 6}. Luego debe mostrar por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas de la carrera, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos.
"""

creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5, 'Contabilidad': 8, 'Programación': 6, 'Redacción': 6, 'Trabajo final': 6}

for asignatura, creditos in creditos.items():
    print(f"{asignatura} tiene {creditos} créditos")

total_creditos = sum(creditos.values())
print("Total de créditos:", total_creditos)


"""3. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. Repetir las preguntas hasta que el usuario ingrese la palabra  fin (fin puede estar en mayúsculas o minúsculas).
"""

precios_frutas = {
    'Banana': 1.35,
    'Manzana': 0.80,
    'Pera': 0.85,
    'Naranja': 0.70
}

while True:
    fruta = input("Ingrese una fruta (o 'fin' para salir): ").capitalize()

    if fruta == 'Fin':
        break

    if fruta in precios_frutas:
        kilos = float(input("Ingrese la cantidad en kilos: "))
        precio_total = precios_frutas[fruta] * kilos
        print(f"El precio de {kilos} kilos de {fruta} es: {precio_total}$")
    else:
        print("La fruta no está en el diccionario.")

"""4. Escribir un programa que permite realizar una estadística de los nombres que llevan los recién nacidos. El programa deberá llevar registro de cada nombre y la cantidad de niños/niñas que lo llevan (solo primer nombre).  Para eso solicitará al usuario que ingrese los nombres por pantalla uno a la vez. Para finalizar, ingresa la cadena vacía y el programa muestra una lista con los nombres y la cantidad de niños con ese nombre.
"""
nombres = {}
while True:
    nombre = input("Ingrese un nombre (o dejar vacío para finalizar): ")
    if nombre == "":
        break
    if nombre in nombres:
        nombres[nombre] += 1
    else:
        nombres[nombre] = 1

for nombre, cantidad in nombres.items():
    print(f"{nombre}: {cantidad} niños")


"""5. Escribir una función que quita los elementos duplicados de una lista utilizando un diccionario. Debe retornar una nueva lista sin elementos repetidos, sin importar el orden.
"""

def quitar_duplicados(lista):
    diccionario = {}
    for elemento in lista:
        diccionario[elemento] = True
    return list(diccionario.keys())


"""6. Escribir una función que recibe el nombre de una canción y retorna el/los artista que la interpretan (utilizando diccionarios). Por ejemplo:
"""
def get_artistas(cancion):
    canciones = {
        'All my loving': 'The Beatles',
        'All along the watchtower': ['Bob Dylan', 'Jimi Hendrix']
    }
    return canciones.get(cancion, "Canción no encontrada")

print(get_artistas('All my loving'))  # 'The Beatles'
print(get_artistas('All along the watchtower'))  # ['Bob Dylan', 'Jimi Hendrix']


"""7. Crear una función que permita determinar probabilísticamente resultados que se pueden obtener en una tirada de un dado. Para eso se deben generar 10.000 tiradas aleatorias y obtener el porcentaje que resulta para cada número posible en el dado.

La función debe devolver un diccionario como el siguiente: {1: 10, 2: 24, 3: 26, 4: 19, 5: 11, 6: 10} donde la clave corresponde al número de la cara del dado (1 a 6) y el valor al porcentaje de tiradas que salió dicho número (en este caso el 1 salió el 10% de las tiradas - 1000 tiradas- ).
"""

import random

def tirada_dado():
    resultados = {}
    for _ in range(10000):
        tirada = random.randint(1, 6)
        if tirada in resultados:
            resultados[tirada] += 1
        else:
            resultados[tirada] = 1

    for numero, cantidad in resultados.items():
        porcentaje = (cantidad / 10000) * 100
        resultados[numero] = porcentaje

    return resultados

print(tirada_dado())


"""8. Escribir una función que permite organizar el envío masivo de emails para propagandas publicitarias. La función recibe un diccionario donde la clave es el nombre de una persona y el valor asociado es una lista de sus direcciones de correo electrónico (“emails”).
"""

def organizar_envio_emails(correos):
    emails_validos = {}

    for persona, direcciones in correos.items():
        direcciones_validas = []
        for direccion in direcciones:
            if direccion.count('@') == 1 and '.' in direccion:
                direcciones_validas.append(direccion)
        emails_validos[persona] = list(set(direcciones_validas))

    return emails_validos

emails = {
    "Martín Rodríguez": ["arodri@ucu.edu.uy", "rodriguez@gmail.com"],
    "Marcela Rodríguez": ["mleites@gmail.com", "rodriguez@gmail.com"],
    "Juan Lamas": ["jlamasucu.edu.uy", "juan.lamas@gmail.com"]
}

print(organizar_envio_emails(emails))


"""Escribir una función que sanitiza una cadena. El método de sanitización es el siguiente:
a. Todas las letras con tilde se cambian por la misma letra sin tilde.

b. Símbolos de pregunta y de exclamación se reemplazan por guiones (“-“)

c. Los espacios se reemplazan por guiones bajos (“_")

d. La "ñ" se reemplaza por la “n"

e. Cualquier otro símbolo (que no sean letras) se remueve."""

def sanitizar_cadena(cadena):
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")
    cadena = cadena.replace("?", "-")
    cadena = cadena.replace("!", "-")
    cadena = cadena.replace(" ", "_")
    cadena = cadena.replace("ñ", "n")
    cadena = ''.join(c for c in cadena if c.isalnum() or c == "_" or c == "-")
    return cadena

print(sanitizar_cadena("¡Hola, cómo estás?"))


""" Definir una función que recibe una cadena de caracteres  y cuente la cantidad de ocurrencias de cada letra del abecedario (sin distinguir mayúsculas de minúsculas).

Ejemplo:
funcion("06/2021: Ejercicios en Python.") 
--> { "E": 3, "J": 1, "R": 1, ... }  """

def contar_letras(cadena):
    contador = {}
    for letra in cadena:
        letra = letra.lower()
        if letra.isalpha():
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
    return contador

resultado = contar_letras("06/2021: Ejercicios en Python.")
print(resultado)


""""El siguiente código Python permite obtener desde Internet el libro "Cuentos de Amor de Locura y de Muerte de Horacio Quiroga" desde el Proyecto Gutenberg (permite descarga gratuita de e-books):

from urllib.request import urlopen
link = 'https://www.gutenberg.org/cache/epub/13507/pg13507.txt'
f = urlopen(link)
myfile = f.read().decode('utf-8')
print(myfile)


La función read() nos devuelve una cadena de caracteres (string) con el contenido completo del libro.

Crear una función que permita obtener las 5 letra más utilizadas en todo el libro."""

from urllib.request import urlopen

def obtener_letras_mas_utilizadas(url):
    f = urlopen(url)
    contenido = f.read().decode('utf-8')
    letras = {}

    for caracter in contenido:
        if caracter.isalpha():
            letra = caracter.lower()
            if letra in letras:
                letras[letra] += 1
            else:
                letras[letra] = 1

    letras_ordenadas = sorted(letras.items(), key=lambda x: x[1], reverse=True)
    letras_top5 = letras_ordenadas[:5]
    return dict(letras_top5)

url = 'https://www.gutenberg.org/cache/epub/13507/pg13507.txt'
resultado = obtener_letras_mas_utilizadas(url)
print(resultado)


"""8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count."""

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From "):
        split = line.split()        
        print(split[1])
        count+=1

print("There were", count, "lines in the file with From as the first word")

####################
#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
handle = open(name)
emailist = []
sender= dict()

#extraer los correos del texto
for line in handle: #recorrer las líneas
    if line.startswith("From "): #definir cual queremos
        linelst = line.split() #pasarla a una lista
        email = linelst[1] #elegir los elementos
        emailist.append(email) #añadirlo a una lista 

#recorrer la lista de correos generada y añadirlo a un diccionario
for dir in emailist:
    sender[dir] = sender.get(dir, 0) + 1 #en el diccionario, añadir la llave del correo que queremos y el valor by default, añadir uno si existe

#recorrer el diccionario y chequear cual es el valor mas grande

bigcount = 0 #almacenar contador de palabras
bigword = 0 #almacenar palabra en la memoria

for word,count in sender.items(): #recorrer los pares clave valor en los items del diccionario
    if bigcount is None or count > bigcount: #si el valor del primer item es 0 entonces creamos el valor
        bigword = word #y reemplazamos el valor existente por el mas grande
        bigcount = count #y reemplazamos el valor existente por el mas grande
print(bigword, bigcount) #imprimir el par clave valor de mas alto valor


#####################################
#IMPRIMIR LAS 10 PALABRAS MAS COMUNES 

lst = [] #tenemos una lista para almacenar pares k, v
dct = {} #y un diccionario ya creado
for key,value in dct.items(): #iteramos sobre los items (k , v) del diccionario que tenemos 
    newtup = (value , key) #lo que salga de ahí, son tuplas que vamos a guardar
    lst.append(newtup) #las guardamos en la lista vacía

#ahora las tenemos que ordenar, porque están ordenadas en value, key order. para que aparezca la key primero y luego el valor

lst = sorted (lst, reverse=True) #con esto las ordenamos de mayor a menor, primero el valor, luego la key
for value , key in lst[:10]: #con esto las vamos a meter en una lista ya volteadas para luego imprimirlas
    print(key , value) #las podemos imprimir en key, value o al revés si queremos

###################################################
# LIST COMPREHENSION
#podemos resumir esto de esta manera:

c = {}
print (sorted([(value,key) for key,value in c.items()]))

#podemos leerlo así:

# [(value,key) for key,value in c.items()] <-- con esto vamos a crear una lista de pares clave valor, iterando sobre un diccionario ya creado. 

# sorted([(value,key) for key,value in c.items()]) <-- con esto lo ordenamos. 
# print (sorted([(value,key) for key,value in c.items()])) <-- al final lo imprimimos


# Función para obtener el menor y el mayor de una lista de precios:
def obtener_minimo_maximo(precios):
    if len(precios) == 0:
        return None
    minimo = maximo = precios[0]
    for precio in precios:
        if precio < minimo:
            minimo = precio
        if precio > maximo:
            maximo = precio
    return minimo, maximo


# Lectura de números desde el teclado y mostrar los números pares:
numeros = []
while True:
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        break
    numeros.append(numero)

numeros_pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", numeros_pares)

#Función para verificar si una cadena está en una lista de cadenas:

def verificar_cadena_en_lista(cadenas, cadena):
    return cadena in cadenas

# Programa para generar una lista con valores aleatorios y mostrar sus cuadrados y cubos:

import random

numeros = [random.randint(1, 10) for _ in range(10)]
for num in numeros:
    print("Número:", num)
    print("Cuadrado:", num ** 2)
    print("Cubo:", num ** 3)
    print()

# Programa para leer las notas de un alumno y mostrar información sobre ellas:


notas = []
for i in range(5):
    nota = float(input("Ingrese la nota {}: ".format(i + 1)))
    notas.append(nota)

print("Notas:", notas)
print("Nota media:", sum(notas) / len(notas))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

# Aquí tienes las funciones para calcular el dígito verificador de la cédula de identidad uruguaya y validar su validez:

def calcular_digito_verificador(cedula):
    cedula_str = str(cedula)
    ponderacion = [4, 3, 6, 7, 8, 9]  # Valores de ponderación
    suma = 0

    if len(cedula_str) == 7:
        ponderacion.insert(0, 2)  # Agregar valor de ponderación para cédulas de 7 dígitos

    for i, digito in enumerate(cedula_str):
        valor = int(digito) * ponderacion[i]
        suma += valor

    resto = suma % 10
    if resto == 0:
        return 0
    else:
        return 10 - resto


def es_cedula_valida(cedula, digito_verificador):
    cedula_str = str(cedula)
    if len(cedula_str) != 6 and len(cedula_str) != 7:
        return False

    calculado = calcular_digito_verificador(cedula)
    return calculado == digito_verificador

cedula = int(input("Ingrese el número de cédula: "))
digito_verificador = int(input("Ingrese el dígito verificador: "))

if es_cedula_valida(cedula, digito_verificador):
    print("La cédula es válida.")
else:
    print("La cédula no es válida.")

# Aquí tienes un programa en Python que solicita números positivos por teclado y los almacena en un conjunto hasta que se alcance un máximo de 5 elementos o se ingrese un número negativo. El programa también muestra un mensaje si el número ingresado ya existe y, al finalizar la carga, muestra el conjunto resultante:

numeros = set()

while len(numeros) < 5:
    numero = int(input("Ingresa un número positivo (ingresa un número negativo para terminar): "))
    
    if numero < 0:
        break
    
    if numero in numeros:
        print("Ese número ya existe.")
    else:
        numeros.add(numero)

print("Conjunto resultante:", numeros)


#Aquí tienes un programa en Python que muestra un menú y realiza diferentes acciones según la opción elegida por el usuario. El programa continúa mostrando el menú hasta que se elija la opción de finalizar:

conjunto = set()

def mostrar_menu():
    print("Menú:")
    print("A: Agregar elemento al conjunto")
    print("B: Borrar elemento del conjunto")
    print("T: Borrar todos los elementos del conjunto")
    print("M: Mostrar conjunto")
    print("F: Finalizar")

def agregar_elemento():
    elemento = int(input("Ingresa el número que deseas agregar: "))
    if elemento in conjunto:
        print("Ese número ya existe en el conjunto.")
    else:
        conjunto.add(elemento)
        print("Número agregado al conjunto.")

def borrar_elemento():
    elemento = int(input("Ingresa el número que deseas borrar: "))
    if elemento in conjunto:
        conjunto.remove(elemento)
        print("Número eliminado del conjunto.")
    else:
        print("Ese número no existe en el conjunto.")

def borrar_todos():
    conjunto.clear()
    print("Todos los elementos han sido borrados del conjunto.")

def mostrar_conjunto():
    print("Conjunto:", conjunto)

mostrar_menu()

while True:
    opcion = input("Elige una opción del menú: ").upper()
    
    if opcion == "A":
        agregar_elemento()
    elif opcion == "B":
        borrar_elemento()
    elif opcion == "T":
        borrar_todos()
    elif opcion == "M":
        mostrar_conjunto()
    elif opcion == "F":
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida del menú.")

    print()  # Salto de línea

print("Programa finalizado.")


#¿Qué elementos están presentes en ambos conjuntos? ¿Cuántos son?

A = {i**2 for i in range(1, 1000)}
B = {i**3 for i in range(1, 1000)}

elementos_comunes = A.intersection(B)
cantidad_elementos_comunes = len(elementos_comunes)

print("Elementos comunes:", elementos_comunes)
print("Cantidad de elementos comunes:", cantidad_elementos_comunes)

#¿El conjunto {576, 676, 784, 529, 625, 729, 7744, 7569} son números obtenidos por elevar un natural al cuadrado?

conjunto_verificar = {576, 676, 784, 529, 625, 729, 7744, 7569}

son_cuadrados = all(numero in A for numero in conjunto_verificar)

if son_cuadrados:
    print("Todos los números son obtenidos por elevar un natural al cuadrado.")
else:
    print("Al menos uno de los números no es obtenido por elevar un natural al cuadrado.")


# Solicitar una cantidad al usuario y luego iterar esa cantidad de veces, solicitando un número en cada iteración y mostrando la suma de todos los números ingresados al final:

cantidad = int(input("Ingrese una cantidad: "))
suma = 0

for _ in range(cantidad):
    numero = int(input("Ingrese un número: "))
    suma += numero

print("La suma de los números ingresados es:", suma)

# 2a. Simular 20 tiradas de dos dados simultáneamente y calcular el promedio de la suma de los resultados:

import random

suma_total = 0

for _ in range(20):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    suma_total += suma

promedio = suma_total / 20
print("El promedio de la suma de los resultados de los dos dados es:", promedio)

#2b. Contar la cantidad de veces que sale cada cara (1 al 6) en 30 tiradas:

import random

contador_caras = [0] * 6

for _ in range(30):
    cara = random.randint(1, 6)
    contador_caras[cara - 1] += 1

for i, cantidad in enumerate(contador_caras):
    print("Cantidad de veces que salió la cara", i + 1, ":", cantidad)

#Permitir al usuario ingresar 6 números enteros, calcular la sumatoria de los números negativos y el promedio de los positivos:

numeros_negativos = 0
suma_positivos = 0
cantidad_positivos = 0

for _ in range(6):
    numero = int(input("Ingrese un número entero: "))
    if numero < 0:
        numeros_negativos += numero
    elif numero > 0:
        suma_positivos += numero
        cantidad_positivos += 1

if cantidad_positivos > 0:
    promedio_positivos = suma_positivos / cantidad_positivos
else:
    promedio_positivos = 0

print("Sumatoria de los números negativos:", numeros_negativos)
print("Promedio de los números positivos:", promedio_positivos)

#Iterar sobre las letras del string ingresado e imprimir cada letra en una línea:

palabra = input("Ingrese una palabra: ")

for letra in palabra:
    print(letra)

#Iterar sobre los índices de las letras y luego imprimir la letra correspondiente en cada línea:

palabra = input("Ingrese una palabra: ")

for i in range(len(palabra)):
    letra = palabra[i]
    print(letra)

#Imprimir las letras del string en orden inverso (una letra por línea):

palabra = input("Ingrese una palabra: ")

for i in range(len(palabra) - 1, -1, -1):
    letra = palabra[i]
    print(letra)


#Reemplazar los espacios en un string por el carácter ";":

def reemplazar_espacios(cadena):
    nueva_cadena = ""
    for caracter in cadena:
        if caracter == " ":
            nueva_cadena += ";"
        else:
            nueva_cadena += caracter
    return nueva_cadena

cadena = input("Ingrese una cadena de caracteres: ")
cadena_reemplazada = reemplazar_espacios(cadena)
print("Cadena resultante:", cadena_reemplazada)

#Convertir una fecha en formato "dd/mm/aaaa" a formato "aaaa-mm-dd":

def convertir_fecha(fecha):
    dia, mes, anio = fecha.split("/")
    nueva_fecha = anio + "-" + mes + "-" + dia
    return nueva_fecha

fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
fecha_convertida = convertir_fecha(fecha)
print("Fecha convertida:", fecha_convertida)


#Verificar si una cadena es un pangrama (contiene todas las letras del alfabeto):

def es_pangrama(cadena):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cadena = cadena.lower()
    for letra in alfabeto:
        if letra not in cadena:
            return False
    return True

cadena = input("Ingrese una cadena de caracteres: ")
if es_pangrama(cadena):
    print("La cadena es un pangrama.")
else:
    print("La cadena no es un pangrama.")

#Verificar si una cadena es un lipograma (contiene todas las letras del alfabeto excepto una):

def es_lipograma(cadena):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cadena = cadena.lower()
    for letra in alfabeto:
        if letra not in cadena:
            return True
    return False

cadena = input("Ingrese una cadena de caracteres: ")
if es_lipograma(cadena):
    print("La cadena es un lipograma.")
else:
    print("La cadena no es un lipograma.")

#Calcular el valor gemátrico de una cadena (suma de los valores de las letras):

def valor_gemátrico(cadena):
    suma = 0
    for letra in cadena:
        if letra.isalpha():
            valor = ord(letra.lower()) - ord("a") + 1
            suma += valor
    return suma

cadena = input("Ingrese una cadena de caracteres: ")
valor = valor_gemátrico(cadena)
print("Valor gemátrico de la cadena:", valor)

#Verificar si una palabra es mágica (tiene un valor gemátrico de 21):

def es_palabra_mágica(palabra):
    valor = valor_gemátrico(palabra)
    return valor == 21

palabra = input("Ingrese una palabra: ")
if es_palabra_mágica(palabra):
    print("La palabra es mágica.")
else:
    print("La palabra no es mágica.")

#Verificar si una palabra es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda):

def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")

# 1. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dolar':'us$', 'Yen':'¥', 'Peso':'$', 'Real':'R$'}, luego pregunte al usuario por una divisa y muestre su símbolo (o un mensaje de aviso si la divisa no está en el diccionario). 

divisas = {'Euro': '€', 'Dolar': 'us$', 'Yen': '¥', 'Peso': '$', 'Real': 'R$'}
divisa = input("Ingrese una divisa: ")

if divisa in divisas:
    simbolo = divisas[divisa]
    print(f"El símbolo de {divisa} es: {simbolo}")
else:
    print("La divisa no está en el diccionario.")

# 2. Escribir un programa que almacene el diccionario con los créditos de las asignaturas de una carrera {'Matemáticas': 6, 'Física': 4, 'Química': 5, 'Contabilidad': 8, 'Programación: 6, 'Redacción': 6, 'Trabajo final': 6}. Luego debe mostrar por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas de la carrera, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos.

creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5, 'Contabilidad': 8, 'Programación': 6, 'Redacción': 6, 'Trabajo final': 6}

total_creditos = 0
for asignatura, creditos in creditos.items():
    print(f"{asignatura} tiene {creditos} créditos.")
    total_creditos += creditos

print("Total de créditos:", total_creditos)

#3. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. Repetir las preguntas hasta que el usuario ingrese la palabra  fin (fin puede estar en mayúsculas o minúsculas).

precios_frutas = {'Banana': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}

while True:
    fruta = input("Ingrese una fruta (o 'fin' para terminar): ").capitalize()

    if fruta == 'Fin':
        break

    if fruta in precios_frutas:
        kilos = float(input("Ingrese el número de kilos: "))
        precio = precios_frutas[fruta] * kilos
        print(f"El precio de {kilos} kilos de {fruta} es: {precio}")
    else:
        print("La fruta no está en el diccionario.")


#4. Escribir un programa que permite realizar una estadística de los nombres que llevan los recién nacidos. El programa deberá llevar registro de cada nombre y la cantidad de niños/niñas que lo llevan (solo primer nombre).  Para eso solicitará al usuario que ingrese los nombres por pantalla uno a la vez. Para finalizar, ingresa la cadena vacía y el programa muestra una lista con los nombres y la cantidad de niños con ese nombre.

nombres = {}
while True:
    nombre = input("Ingrese un nombre (deje vacío para terminar): ")
    
    if nombre == "":
        break
    
    if nombre in nombres:
        nombres[nombre] += 1
    else:
        nombres[nombre] = 1

for nombre, cantidad in nombres.items():
    print(f"{nombre}: {cantidad}")

# Aquí tienes la función que elimina elementos duplicados de una lista utilizando un diccionario:

def eliminar_duplicados(lista):
    diccionario = {}
    for elemento in lista:
        diccionario[elemento] = None
    return list(diccionario.keys())


#Aquí tienes la función que busca el artista de una canción utilizando diccionarios:

def get_artistas(cancion):
    artistas = {
        'All my loving': 'The Beatles',
        'All along the watchtower': ['Bob Dylan', 'Jimi Hendrix']
    }
    return artistas.get(cancion)

#Aquí tienes la función que realiza una tirada de un dado y calcula la probabilidad de cada resultado:
import random

def tirar_dado():
    resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    total_tiradas = 10000

    for _ in range(total_tiradas):
        resultado = random.randint(1, 6)
        resultados[resultado] += 1

    probabilidades = {}
    for resultado, cantidad in resultados.items():
        porcentaje = cantidad / total_tiradas * 100
        probabilidades[resultado] = round(porcentaje, 2)

    return probabilidades

#Aquí tienes la función que organiza el envío masivo de emails y elimina emails duplicados o inválidos:

def organizar_envio_emails(emails):
    emails_validos = {}

    for persona, direcciones in emails.items():
        direcciones_validas = []
        for direccion in direcciones:
            if direccion.count('@') == 1 and '.' in direccion:
                direcciones_validas.append(direccion)
        if direcciones_validas:
            emails_validos[persona] = direcciones_validas

    return emails_validos


#Aquí tienes la función que sanitiza una cadena:

def sanitizar_cadena(cadena):
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        '¿': '-', '?': '-', '¡': '-', '!': '-',
        ' ': '_', 'ñ': 'n', 'Ñ': 'N'
    }

    cadena_sanitizada = ""
    for caracter in cadena:
        if caracter in reemplazos:
            cadena_sanitizada += reemplazos[caracter]
        elif caracter.isalpha():
            cadena_sanitizada += caracter

    return cadena_sanitizada

#Aquí tienes la función que cuenta la cantidad de ocurrencias de cada letra del abecedario en una cadena:

def contar_letras(cadena):
    contador_letras = {}

    for caracter in cadena:
        caracter = caracter.lower()
        if caracter.isalpha():
            if caracter in contador_letras:
                contador_letras[caracter] += 1
            else:
                contador_letras[caracter] = 1

    return contador_letras

#Aquí tienes la función que obtiene las 5 letras más utilizadas en un libro:

def obtener_letras_mas_utilizadas(libro):
    contador_letras = {}
    
    for letra in libro:
        letra = letra.lower()
        if letra.isalpha():
            if letra in contador_letras:
                contador_letras[letra] += 1
            else:
                contador_letras[letra] = 1

    letras_mas_utilizadas = sorted(contador_letras, key=contador_letras.get, reverse=True)[:5]

    return letras_mas_utilizadas

# Función para contar la cantidad de veces que una cadena aparece en un archivo:
def contar_cadena_en_archivo(archivo_nombre, cadena):
    with open(archivo_nombre, "r") as archivo:
        contenido = archivo.read()
        cantidad = contenido.count(cadena)
    return cantidad

# Función para intercalar líneas de dos archivos en uno nuevo:
def intercalar_archivos(archivo1_nombre, archivo2_nombre, archivo_nuevo_nombre):
    with open(archivo1_nombre, "r") as archivo1, open(archivo2_nombre, "r") as archivo2, open(archivo_nuevo_nombre, "w") as archivo_nuevo:
        lineas1 = archivo1.readlines()
        lineas2 = archivo2.readlines()
        max_lineas = max(len(lineas1), len(lineas2))
        
        for i in range(max_lineas):
            if i < len(lineas1):
                archivo_nuevo.write(lineas1[i])
            if i < len(lineas2):
                archivo_nuevo.write(lineas2[i])

# Función para ingresar texto y guardarlo en un archivo:
def ingresar_y_guardar_texto():
    texto = ''
    while True:
        entrada = input("Ingrese texto (ingrese '::q' para finalizar): ")
        if entrada == '::q':
            break
        texto += entrada + '\n'
    
    archivo_nombre = input("Ingrese nombre de archivo para guardar el texto: ")
    
    with open(archivo_nombre, 'w') as archivo:
        archivo.write(texto)
    
    ver_texto = input("¿Desea ver el texto guardado? (s/n): ")
    if ver_texto.lower() == 's':
        with open(archivo_nombre, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)

# Función para buscar una cadena en un archivo y obtener los números de línea:
def buscar_cadena_en_archivo(archivo_nombre, cadena):
    lineas_encontradas = []
    with open(archivo_nombre, "r", encoding='utf8', errors="ignore") as archivo:
        for i, linea in enumerate(archivo, start=1):
            if cadena in linea:
                lineas_encontradas.append(i)
    return lineas_encontradas

# Función para concatenar archivos en uno solo:
def concatenar_archivos(lista_archivos, archivo_nuevo_nombre):
    with open(archivo_nuevo_nombre, 'w') as archivo_nuevo:
        for archivo_nombre in lista_archivos:
            with open(archivo_nombre, 'r') as archivo:
                contenido = archivo.read()
                archivo_nuevo.write(contenido)

# Clases y función para manejar notas de alumnos:
class Nota:
    def __init__(self, cedula, nombre, nota):
        self.cedula = cedula
        self.nombre = nombre
        self.nota = nota
    
    def get_cedula(self):
        return self.cedula
    
    def get_nombre(self):
        return self.nombre
    
    def get_nota(self):
        return self.nota
    
    def set_nota(self, nueva_nota):
        self.nota = nueva_nota


class Grupo:
    def __init__(self, nombre_grupo, salon):
        self.nombre_grupo = nombre_grupo
        self.salon = salon
        self.notas = []
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
    
    def grabar_resultados_aprobados(self):
        aprobados = [nota for nota in self.notas if nota.get_nota() >= 61]
        aprobados = sorted(aprobados, key=lambda x: x.get_nota(), reverse=True)
        
        with open('ResultadosP1.txt', 'w') as archivo:
            for nota in aprobados:
                archivo.write(f"{nota.get_nombre()}: {nota.get_nota()}\n")


def cargar_notas_desde_archivo(archivo_notas):
    notas = []
    with open(archivo_notas, 'r') as archivo:
        for linea in archivo:
            cedula, nombre, nota = linea.strip().split(',')
            nota_obj = Nota(cedula, nombre, int(nota))
            notas.append(nota_obj)
    return notas

# Programa para procesar información de clientes desde un archivo CSV:
import csv

def procesar_informacion_clientes(archivo_origen, opciones_procesamiento, archivo_salida):
    separador = ','
    columnas_incluidas = []
    nueva_columna_valor = None

    for opcion in opciones_procesamiento:
        if opcion.startswith('-s='):
            separador = opcion[3:]
        elif opcion.startswith('-c='):
            columnas_incluidas = list(map(int, opcion[3:].split(',')))
        elif opcion.startswith('-a='):
            nueva_columna_valor = opcion[3:]
        elif opcion.startswith('-o='):
            archivo_salida = opcion[3:]
    
    datos_salida = []
    with open(archivo_origen, 'r') as archivo_origen:
        lector_csv = csv.reader(archivo_origen, delimiter=separador)
        for fila in lector_csv:
            fila_salida = []
            if columnas_incluidas:
                for indice in columnas_incluidas:
                    if indice < len(fila):
                        fila_salida.append(fila[indice])
            else:
                fila_salida = fila
            
            if nueva_columna_valor is not None:
                fila_salida.append(nueva_columna_valor)
            
            datos_salida.append(fila_salida)
    
    with open(archivo_salida, 'w', newline='') as archivo_salida:
        escritor_csv = csv.writer(archivo_salida, delimiter=separador)
        escritor_csv.writerows(datos_salida)

#Ejercicio 1: Conversión de sistema binario a decimal

def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)
    
    for i in range(longitud):
        bit = int(binario[i])
        decimal += bit * (2 ** (longitud - 1 - i))
    
    return decimal

# Ejemplos de conversión de binario a decimal
binario_1 = "10011110"
binario_2 = "1110"
binario_3 = "0"
binario_4 = "10"
binario_5 = "1"

print(binario_a_decimal(binario_1))  # Resultado: 158
print(binario_a_decimal(binario_2))  # Resultado: 14
print(binario_a_decimal(binario_3))  # Resultado: 0
print(binario_a_decimal(binario_4))  # Resultado: 2
print(binario_a_decimal(binario_5))  # Resultado: 1


#Ejercicio 2: Conversión de sistema decimal a binario

def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    
    while decimal > 0:
        bit = decimal % 2
        binario = str(bit) + binario
        decimal = decimal // 2
    
    return binario

# Ejemplos de conversión de decimal a binario
decimal_1 = 32
decimal_2 = 147
decimal_3 = 7512
decimal_4 = 145
decimal_5 = 1
decimal_6 = 0

print(decimal_a_binario(decimal_1))  # Resultado: "100000"
print(decimal_a_binario(decimal_2))  # Resultado: "10010011"
print(decimal_a_binario(decimal_3))  # Resultado: "1110101011000"
print(decimal_a_binario(decimal_4))  # Resultado: "10010001"
print(decimal_a_binario(decimal_5))  # Resultado: "1"
print(decimal_a_binario(decimal_6))  # Resultado: "0"

#Ejercicio 3: Conversión de decimal a binario (función)

def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    
    while decimal > 0:
        bit = decimal % 2
        binario = str(bit) + binario
        decimal = decimal // 2
    
    return binario

# Ejemplo de uso de la función
numero_decimal = 42
numero_binario = decimal_a_binario(numero_decimal)
print(numero_binario)  # Resultado: "101010"


#Conversión de binario a decimal (función)

def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)
    
    for i in range(longitud):
        bit = int(binario[i])
        decimal += bit * (2 ** (longitud - 1 - i))
    
    return decimal

# Ejemplo de uso de la función
numero_binario = "1101"
numero_decimal = binario_a_decimal(numero_binario)
print(numero_decimal)  # Resultado: 13

# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

def summation(num):
    return sum(range(1,num + 1))

# Complete the solution so that it reverses the string passed into it.

def solution(str):
    return str[::-1]

#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    txtlst = text.split()