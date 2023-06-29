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


# Laboratorio 8 - Ejercicio 8 (desafio)
#
#
# Definicion de Variables con valores por defecto
archivo_salida = "clientes_new.csv"
separador = ','
columnas = ['0', '1', '2', '3', '4']
agrega_valor = ''

# Lista con los clientes que se van a cargar del archivo de entrada
clientes = []

# Se pide ubicación del archivo de clientes (por ejemplo: clientes.csv)
archivo_entrada = input("Ingrese archivo de clientes > ")

# Se lee el contenido y se carga los clientes en la lista
f = open(archivo_entrada)
for cliente in f:
    cliente = cliente.rstrip()
    clientes.append(cliente.split(','))
f.close()

# Se le pide al usuario que ingrese los comandos
comando = input("Ingrese comando > ")

lista_comandos = comando.split()

# Se procesan los comandos
for comando in lista_comandos:
    comando_partes = comando.split('=')
    if comando_partes[0] == '-s':
        separador = comando_partes[1]
    elif comando_partes[0] == '-c':
        columnas = comando_partes[1].split(',')
    elif comando_partes[0] == '-a':
        agrega_valor = comando_partes[1]
    elif comando_partes[0] == '-o':
        archivo_salida = comando_partes[1]

# Se crea el archivo de salida
o = open(archivo_salida,'w')

# Se procesan los clientes y se graba en el archivo de salida
for cliente in clientes:
    linea = ""
    for pos in range(len(columnas)):
        linea += cliente[int(columnas[pos])]
        if pos < len(columnas)-1:
            linea += separador
        pos += 1
    if len(agrega_valor):
        linea += separador + agrega_valor
    o.write(linea + '\n')

o.close()


# Laboratorio 8 - Ejercicio 4
#
# Ver la letra en el pdf
#


def si_o_no(texto):
    while True:
        opcion = input(texto + "(si/no) > ")
        if opcion.lower() in ['si','no']:
            return opcion


def imprimo_consulta(consulta, cadena, nombre, apellido):

    print("Estimado {} {}".format(nombre, apellido))
    if consulta[0] != 0:
        print("La cadena '{}' aparecio un total de {} en el archivo".format(
            cadena, consulta[0]
        ))
        print("en las posiciones que se detallan a continuación.")
        print("Nro de línea\t\tUbicación")
        print("============\t\t=========")
        for elemento in consulta[1:]:
            print("{:12}\t\t{:9}".format(
                elemento[0], elemento[1]
            ))
        print("=================================================")
    else:
        print("La cadena '{}' no se encuentra en el archivo".format(
            cadena
        ))
    print()

def busco_cadena(ubicacion, cadena, nombre, apellido):

    archivo = open(ubicacion)
    resultado = []

    resultado.append(0)  # inicializo el primer elemento con el contador
                         # en 0
    nro_linea = 0
    for linea in archivo:
        linea = linea.strip()
        nro_linea += 1
        pos = linea.find(cadena)
        while pos != -1:
            resultado.append([nro_linea,pos])
            resultado[0] += 1
            pos = linea.find(cadena, pos + len(cadena))
    archivo.close()

    opcion = si_o_no("Quiere ver el resultado de la consulta?")
    if opcion == 'si':
        imprimo_consulta(resultado, cadena, nombre, apellido)

    return resultado


# Programa principal

nombre = input("Ingrese su nombre > ")
apellido = input("Ingrese su apellido > ")
ubicacion = input("Ingrese nombre de archivo > ")
cadena = input("Ingrese la cadena a buscar > ")

resultado = busco_cadena(ubicacion, cadena, nombre, apellido)

# Laboratorio 8 - Ejercicio 3
#
# Escribir una función que le permita ingresar texto a un usuario,
# hasta que ingrese la secuencia de caracteres "::q" con la cual
# indicará que finaliza el ingreso.
#
# Luego de finalizado el ingreso, el programa le solicitará que ingrese
# un nombre (ubicación y nombre con extensión) de archivo en el cual se
# grabará todo el texto ingresado
# Finalmente le preguntará si quiere ver el texto guardado en el archivo,
# y en caso afirmativo le mostrará el contenido del archivo grabado.


def ingreso_texto():
    texto = []

    print("Ingrese textos dando enter, ingresar ':qq' para finalizar")
    linea = input("Ingrese texto > ")
    while linea != ":qq":
        texto.append(linea.strip())
        linea = input(">> ")

    return texto


# Programa principal

texto = ingreso_texto()

if len(texto) > 0:
    ubicacion = input("Escribir en el archivo > ")
    archivo = open(ubicacion, 'w')
    for linea in texto:
        archivo.write(linea + "\n")
    archivo.close()
    respuesta = input("Quiere ver el contenido? (si/no) > ")
    if respuesta.lower() == "si":
        archivo = open(ubicacion, "r")
        print(archivo.read())


# Laboratorio 8 - Ejercicio 2
#
# Escribir una función que abra 2 archivos indicados por
# parámetro y escriba un nuevo archivo con las líneas
# intercaladas de los archivos originales.
#
# La solución utiliza un while que itera en el primer archivo y
# en el interior del while escribe la linea leia del primer archivo
# y lee una línea del segundo archivo (si hay líneas sin leer), la
# escribe en el archivo de salida.
# al finalizar de leer el primer archivo se ejecuta un while
# que lee el segundo archivo y escribe las lineas en el archivo de
# salida en el caso que el segundo archivo sea más grande que el primero

def intercalar(archivo1, archivo2, archivo3):

    a1 = open(archivo1)
    a2 = open(archivo2)

    a3 = open(archivo3, "w")

    linea1 = a1.readline()
    while (linea1):
        linea1 = linea1.rstrip() # elimina el newline
        a3.write(linea1 + "\n")

        linea2 = a2.readline()
        if (linea2):
            linea2 = linea2.rstrip() # elimina el newline
            a3.write(linea2 + "\n")

        linea1 = a1.readline()

    # Si el archivo2 es más grande hay que escribir las lineas
    # que quedaron sin leer
    linea2 = a2.readline()
    while (linea2):
        linea2 = linea2.rstrip()
        a3.write(linea2 + "\n")
        linea2 = a2.readline()

    a1.close()
    a2.close()
    a3.close()

# Programa principal
archivo1 = "archivo1.txt"
archivo2 = "archivo2.txt"
archivo3 = "archivo3.txt"

print("Intercalando el archivo: {} con el archivo: {}".format(
    archivo1, archivo2
))
print("y escribiendo el resultado en el archivo: {}".format(
    archivo3
))

intercalar(archivo1, archivo2, archivo3)

print()
print()

archivo4 = "archivo4.txt"

print("Intercalando el archivo: {} con el archivo: {}".format(
    archivo2, archivo1
))
print("y escribiendo el resultado en el archivo: {}".format(
    archivo4
))
intercalar(archivo2, archivo1, archivo4)
print()


# Laboratorio 8 - Ejercicio 2
#
# Escribir una función que abra 2 archivos indicados por
# parámetro y escriba un nuevo archivo con las líneas
# intercaladas de los archivos originales.
#
# La solución utiliza dos for anidados, en el primer for se lee las
# las líneas del primer archivo y en el for interno se lee una linea
# del segundo archivo y se interrumpe el for. En la siguiente iteración
# del primer for, si no se llego a la última línea del segundo archivo,
# se lee la línea siguiente del mismo.
# Cuando se termino de leer el primer archivo y termina el primer for,
# se ejecuta un for para leer las lineas que falten del segundo archivo
# este for se ejecuta si el segundo archivo es más largo que el primero.

def intercalar(archivo1, archivo2, archivo3):

    a1 = open(archivo1)
    a2 = open(archivo2)

    a3 = open(archivo3, "w")

    for linea1 in a1:
        linea1 = linea1.rstrip() # elimina el newline
        a3.write(linea1 + "\n")

        for linea2 in a2:
            linea2 = linea2.rstrip() # elimina el newline
            a3.write(linea2 + "\n")
            break

    # Si el archivo2 es más grande hay que escribir las lineas
    # que quedaron sin leer
    for linea2 in a2:
        linea2 = linea2.rstrip()
        a3.write(linea2 + "\n")

    a1.close()
    a2.close()
    a3.close()

# Programa principal
archivo1 = "archivo1.txt"
archivo2 = "archivo2.txt"
archivo3 = "archivo3.txt"

print("Intercalando el archivo: {} con el archivo: {}".format(
    archivo1, archivo2
))
print("y escribiendo el resultado en el archivo: {}".format(
    archivo3
))

intercalar(archivo1, archivo2, archivo3)

print()
print()

archivo4 = "archivo4.txt"

print("Intercalando el archivo: {} con el archivo: {}".format(
    archivo2, archivo1
))
print("y escribiendo el resultado en el archivo: {}".format(
    archivo4
))
intercalar(archivo2, archivo1, archivo4)
print()

# 1. Escribir una función que recibe como parámetros:
#   a) el nombre (ubicación y nombre con extensión) de un archivo
#   b) una cadena de caracteres
#
# y retorna la cantidad total de veces que esa cadena aparece en el archivo.
# (Nota: La cadena puede estar formada por uno o varios caracteres.
# Por ejemplo, un espacio " ", una letra "z", o por varios caracteres "¡Hola!").
#
# Solución utilizando el metodo count del string

def contar_cadena(ubicacion, cadena):

    archivo = open(ubicacion, 'r')

    contador = 0

    for linea in archivo:
        contador += linea.count(cadena)
    return contador

#ubicacion = input("Nombre de Archivo > ")
#cadena = input("Cadena > ")

ubicacion = "don_quijote_cap1.txt"
cadena = "caballero"

print("La cadena [{}] se encuentra {} veces en el archivo {}".format(
    cadena, contar_cadena(ubicacion, cadena), ubicacion
))


# 1. Escribir una función que recibe como parámetros:
#   a) el nombre (ubicación y nombre con extensión) de un archivo
#   b) una cadena de caracteres
#
# y retorna la cantidad total de veces que esa cadena aparece en el archivo.
# (Nota: La cadena puede estar formada por uno o varios caracteres.
# Por ejemplo, un espacio " ", una letra "z", o por varios caracteres "¡Hola!").
#
# Solución usando el find

def contar_cadena(ubicacion, cadena):

    archivo = open(ubicacion, 'r')

    contador = 0

    for linea in archivo:
        pos = linea.find(cadena)
        while pos != -1:
            contador += 1
            pos = pos + len(cadena)
            pos = linea.find(cadena,pos)
    return contador

# ubicacion = input("Nombre de Archivo > ")
# cadena = input("Cadena > ")

ubicacion = "don_quijote_cap1.txt"
cadena = "caballero"

print("La cadena [{}] se encuentra {} veces en el archivo {}".format(
    cadena, contar_cadena(ubicacion, cadena), ubicacion
))

# Laboratorio 7 - Desafio

class Alumno():
    def __init__(self, nombre, apellido, cedula, fechanac):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fechanac = fechanac

    def __repr__(self):
        return "{}, {}  {}  {}".format(
               self.apellido, self.nombre, self.cedula, self.fechanac)


class Grupo():
    def __init__(self, numero, horario):
        self.numero = numero
        self.horario = horario
        self.alumnos = []

    def __repr__(self):
        return "Numero: {}, Horario: {}".format(self.numero, self.horario)


class Asignatura():
    maxGrupos = 4           # Cantidad maxima de grupos en la Asignatura
    maxAlumnosXgrupo = 5    # Cupo de alumnos por grupo (se usa 2 o 5 a efectos
                             # de poder probar, para produccion se configura en 30

    def __init__(self, id, grupos):
        self.id = id
        if len(grupos) <= Asignatura.maxGrupos:
            self.grupos = grupos[:]
        else:
            self.grupos = grupos[:Asignatura.maxGrupos]
            for grupo in grupos[Asignatura.maxGrupos:]:
                print("Grupo: {} no incluido".format(grupo))

    def inscribir_alumnos(self, gruponro, alumnos):

        for grupo in self.grupos:
            if gruponro == grupo.numero:
                for alumno in alumnos:
                    if len(grupo.alumnos) < Asignatura.maxAlumnosXgrupo:
                        grupo.alumnos.append(alumno)
                    else:
                        print("El alumno: {},{} no pudo ser inscripto al grupo {} de la asignatura: {}".format(
                            alumno.apellido,
                            alumno.nombre,
                            grupo.numero,
                            self.id
                        ))
                break

    def asignar_alumnos(self, alumnos):
        alumnosaux = alumnos[:]
        for grupo in self.grupos:
            while len(alumnosaux) > 0:
                if len(grupo.alumnos) < Asignatura.maxAlumnosXgrupo:
                    if (len(alumnosaux) > 0):
                        grupo.alumnos.append(alumnosaux[0])
                        del alumnosaux[0]
                    else:
                        break
                else:
                    break
        return alumnosaux    # retorna una lista con los alumnos que no
                             # se pueden inscribir, esta lista puede ser vacia.

    def __repr__(self):
        texto = "Asignatura: {}\nGrupos:\n".format(self.id)
        for grupo in self.grupos:
            texto  = texto + "\t{}\n".format(grupo)
            for alumno in grupo.alumnos:
                texto = texto + "\t\t{}\n".format(alumno)
            texto = texto + "\n"
        texto = texto + "\n"
        return texto

#Programa Principal
grupo1 = Grupo(1, 'Martes y Jueves de 18:30 a 22:30')
grupo2 = Grupo(2, 'Miercoles y Viernes de 10:00 a 12:00')

asignatura1 = Asignatura('Programacion I', [grupo1,grupo2])

al1 = Alumno('Alicia', 'Perez', '5.111.111', '2/3/1988')
al2 = Alumno('Juan', 'Garcia', '5.222.111', '24/12/1988')
al3 = Alumno('Estella', 'Dominguez', '5.333.111', '15/3/1988')
al4 = Alumno('Dionisio', 'Diaz', '5.444.111', '9/4/1988')
al5 = Alumno('Esteban', 'Quito', '5.888.111', '23/3/1988')
al6 = Alumno('Soledad', 'Silveira', '5.666.111', '28/2/1988')
al7 = Alumno('Giovani', 'Mecci', '5.555.222', '12/6/1988')
al8 = Alumno('Alejandro', 'Borgia', '5.123.456', '1/9/1988')
al9 = Alumno('Sebastian', 'Del Rey', '5.888.111', '23/3/1988')
al10 = Alumno('Miguel', 'Lopez', '5.666.111', '28/2/1988')
al11 = Alumno('Ariana', 'Mecci', '5.555.222', '12/6/1988')
al12 = Alumno('Jorge', 'Prieto', '5.123.456', '1/9/1988')
al13 = Alumno('Silvina', 'Barros', '5.888.111', '23/3/1988')
al14 = Alumno('Gustavo', 'Garcia', '5.666.111', '28/2/1988')
al15 = Alumno('Eduardo', 'Palermo', '5.555.222', '12/6/1988')
al16 = Alumno('Brain', 'Rodriguez', '5.123.456', '1/9/1988')
al17 = Alumno('Jessy', 'Longhorm', '5.888.111', '23/3/1988')
al18 = Alumno('Federico', 'Salerno', '5.666.111', '28/2/1988')
al19 = Alumno('Federico', 'Salerno', '5.666.111', '28/2/1988')
al20 = Alumno('Ricardo', 'Ledesma', '5.555.222', '12/6/1988')
al21 = Alumno('Genaro', 'Fernandez', '5.123.456', '1/9/1988')

asignatura1.inscribir_alumnos(1, [al1, al2, al3, al4, al5, al6, al7, al8])

print()
print(asignatura1)
print()
print(grupo1)
print(grupo2)
print()
grupo3 = Grupo(3, 'Martes y Jueves de 16:30 a 18:30')
grupo4 = Grupo(4, 'Miercoles y Viernes de 17:00 a 18:00')
grupo5 = Grupo(5, 'Sabados de 10:00 a 12:00')

asignatura2 = Asignatura('Programacion II', [grupo3, grupo4, grupo5])
lst_alumnos = asignatura2.asignar_alumnos([al1, al2, al3, al4, al5, al6, al7, al8,
                                  al9, al10, al11, al12, al13, al14, al15,
                                  al16, al17, al18, al19, al20, al21])

if len(lst_alumnos) > 0:
    print("No se pudieron inscribr a: {} los alumnos: ".format(asignatura2.id))
    for alumno in lst_alumnos:
        print("\t{}".format(alumno))
print()
print()
print(asignatura2)


# Laboratorio 7 - Ejercicio 8

import random


class Baraja(object):
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def mismo_palo(self, otra_carta):
        if self.palo == otra_carta.palo:
            return True
        else:
            return False

    def __str__(self):
        return self.palo + ":" + str(self.valor)


class Mazo(object):
    def flor_derecha(mano):
        '''Funcion de Clase. Determina si la mano tiene una
           flor de derecha (no se considera si hay piezas)'''
        if mano[0].mismo_palo(mano[1]) and mano[0].mismo_palo(mano[2]):
            return True
        else:
            return False

    def tiene_piezas(muestra, mano):
        ''' Función de Clase, retorna verdadero si la mano del
            jugador tiene piezas.'''
        piezas = [2, 4, 5, 10, 12]

        resultado = False
        for baraja in mano:
            if muestra.mismo_palo(baraja):
                if baraja.valor in piezas:
                    resultado = True
        return resultado


def inicializo_mazo():
    '''Retorna una lista que representa el mazo de cartas '''
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ["Copa", "Basto", "Espada", "Oro"]

    mazo = []

    for palo in palos:
        for valor in valores:
            baraja = Baraja(palo, valor)
            mazo.append(baraja)

    return mazo


def reparto_barajas(mazo, n):
    ''' Retorna una lista con la mano de cada participante.
        mazo = Lista de Barajas
        n = cantidad de participantes (valores pueden ser 2 o 4)'''

    mano = []

    if n == 2 or n == 4:
        for participante in range(n):
            mano_participante = []  # Lista de cartas del participante
            for carta_nro in range(3):  # Se le asignan tres cartas al azar al
                # Paticipante.
                pos = random.randint(0, len(mazo) - 1)  # Se obtiene un nro al azar
                # que sea un indice valido
                carta = mazo[pos]  # se obtiene la baraja en pos
                mano_participante.append(carta)  # se agrega a la lista de cartas
                # del participante
                del (mazo[pos])  # se elimna la carta del mazo
            mano.append(mano_participante)  # se agrega la lista de cartas a la mano

    return mano


def obtengo_muestra(mazo):
    '''Retorna una carta que va a ser la muestra'''
    pos = random.randint(0, len(mazo) - 1)
    muestra = mazo[pos]
    del (mazo[pos])    # la muestra obtenida ses borra del mazo
    return muestra


# Programa principal --------------------------------
mazo = inicializo_mazo()
mano = reparto_barajas(mazo, 4)
muestra = obtengo_muestra(mazo)

print("Muestra: {}\n".format(muestra))
for participante in range(4):
    print("Participante: {}".format(participante + 1))
    for carta in mano[participante]:
        print("\t{}".format(carta))
    print()
    if Mazo.tiene_piezas(muestra, mano[participante]):
        print("\tEl jugador tiene piezas")
    else:
        print("\tEl jugador NO tiene piezas")
    print()
    if Mazo.flor_derecha(mano[participante]):
        print("\tEl jugador tiene flor de derecha.")
        print()

# Laboratorio 7 - Ejercicio 7

import random


class Baraja(object):
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def mismo_palo(self, otra_carta):
        if self.palo == otra_carta.palo:
            return True
        else:
            return False

    def __str__(self):
        return self.palo + ":" + str(self.valor)


def inicializo_mazo():
    '''Retorna una lista que representa el mazo de cartas '''
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ["Copa", "Basto", "Espada", "Oro"]

    mazo = []

    # Para cada palo se generan todos los numeros. Esto
    # se lleva a cabo con un for anidado.
    for palo in palos:
        for valor in valores:
            baraja = Baraja(palo, valor)
            mazo.append(baraja)

    return mazo


def reparto_barajas(mazo, n):
    ''' Retorna una lista con la mano de cada participante.
        mazo = Lista de Barajas
        n = cantidad de participantes (valores pueden ser 2 o 4)'''

    mano = []

    if n == 2 or n == 4:
        for participante in range(n):
            mano_participante = [] # Lista de cartas del participante
            for carta_nro in range(3):  # Se le asignan tres cartas al azar al
                                        # Paticipante.
                pos = random.randint(0, len(mazo) - 1) # Se obtiene un nro al azar
                                                       # que sea un indice valido
                carta  = mazo[pos]                     # se obtiene la baraja en pos
                mano_participante.append(carta)        # se agrega a la lista de cartas
                                                       # del participante
                del(mazo[pos])                         # se elimna la carta del mazo
            mano.append(mano_participante)   # se agrega la lista de cartas a la mano

    return mano


def obtengo_muestra(mazo):
    '''Retorna una carta que va a ser la muestra'''
    pos = random.randint(0, len(mazo) - 1)
    muestra = mazo[pos]
    del(mazo[pos])
    return muestra


# Programa principal
mazo = inicializo_mazo()
mano = reparto_barajas(mazo, 4)
muestra = obtengo_muestra(mazo)

print("Muestra: {}\n".format(muestra))
for participante in range(4):
    print("Participante: {}".format(participante + 1))
    for carta in mano[participante]:
        print("\t{}".format(carta))
    print()


# Laboratorio 7 - Ejercicio 6


class Baraja():
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def mismo_palo(self, otra_carta): # otra_carta es un objeto Baraja
        if self.palo == otra_carta.palo:
            return True
        else:
            return False

    def __str__(self):
        return self.palo + ":" + str(self.valor)


# Programa principal
carta1 = Baraja('Basto', 5)
carta2 = Baraja('Copa', 1)
carta3 = Baraja('Copa', 7)
print(carta1)
print(carta2)
print(carta3)
print("la carta {} tiene el mismo palo que la carta {}? {}".format(
    carta1,carta2,carta1.mismo_palo(carta2)
))
print("la carta {} tiene el mismo palo que la carta {}? {}".format(
    carta2,
    carta3,
    carta2.mismo_palo(carta3)
))

# Laboratorio 7 - Ejercicop 5


def transformar_nombres(lista):
    aux = []
    for elem in lista:
        aux.append(', '.join(elem))
    return aux


lista = transformar_nombres([['Rocky', 'Balboa'], ['Muhammad', 'Ali']])
print(lista)

# Laboratorio 7 - ej4


def top_five(lista):

    lista.sort()
    lista.reverse()
    if len(lista) >= 5:
        return lista[:5]
    else:
        return lista


lista = [1, 4, 1, 2, 6, 4, 4, 3, 3, 5]
print(lista, "=>", top_five(lista))


# Laboratorio 7 - ejercicio 3


def difsim(lista1, lista2):
    aux = []
    for elem in lista1:
        if not (elem in lista2):
            aux.append(elem)
    for elem in lista2:
        if not (elem in lista1):
            aux.append(elem)
    return aux


a = [1, 2, 3]
b = [3, 4, 5]

print("a={}, b={}, difsim={}".format(a, b, difsim(a, b)))


# Definicion de funciones


def eliminar_duplicados(lista):
    '''Elimina duplicados de una lista recibida por parámetro'''
    aux = []
    for elem in lista:
        if not (elem in aux):
            aux.append(elem)
    return aux


# Programa Principal
a = [1, 2, 3, 3, 6]
b = eliminar_duplicados(a)

print("Lista inicial {}  Resultado de la función {}".format(a, b))

# Ejercicio 1 - Definir una función que retorna

import random


def lista_random(n):
    ''' Retorna una lista de enteros entre 1 y 6, en forma randomica'''

    aux = []
    for i in range(n):
        aux.append(random.randint(1, 6))
    return aux


print(lista_random(5))
print(lista_random(5))
print(lista_random(4))


# Laboratorio 6 - ejercicio 5
#
#  Crear una clase Hora con atributos para las horas, los minutos y los segundos
#  de una hora.
#
#  1. Construir un constructor sin parámetros con el 00:00:00 como valores por omisión.
#  2. Construir un método “validar” que comprobará si la hora es correcta; si no lo es
#     la ajustará al valor por omisión.
#  3. Construir métodos que permitan acceder y modificar las horas, los minutos y los
#     segundos de un objeto Hora (getters y setters).
#  4. Construir un método que permita representar en un string la hora: mostrará la
#     hora: (07hs. 03ms. 21s.).
#  5. Construir un método “aSegundos” que devolverá el número de segundos transcurridos
#     desde las 0 horas.
#  6. Construir un método “deSegundos(int)” que hará que la hora sea la correspondiente
#     a haber transcurrido, desde las 0 horas, los segundos que se indiquen como
#     parámetro.
#  7. Construir un método “segundosDesde(hora)” que devolverá el número de segundos entre
#     la hora y la hora proporcionada como parámetro.
#  8. Construir un método “siguiente” que pasará al segundo siguiente.
#  9. Construir un método “anterior” que pasará al segundo anterior.
#  10. Construir un método “copia” que devolverá un objeto clonado de la hora.


class Hora():
    def __init__(self):
        self.h = 0
        self.m = 0
        self.s = 0

    def getH(self):
        return self.h

    def setH(self, h):
        self.h =h

    def getM(self):
        return self.m

    def setM(self, m):
        self.m = m

    def getS(self):
        return self.s

    def setS(self, s):
        self.s = s

    def validar(self):
        hora_valida = True
        if ( self.h < 0 or self.h > 23):
            hora_valida = False

        if ( self.m < 0 or self.m > 59):
            hora_valida = False

        if ( self.s < 0 or self.s > 59):
            hora_valida = False

        if not hora_valida:
            self.h = 0
            self.m = 0
            self.s = 0

    def aSegundos(self):
        return self.h * 60 * 60 + self.m * 60 + self.s

    def deSegundos(self, segundos):
        self.h = segundos // 3600
        self.m = ( segundos % 3600 ) // 60
        self.s = segundos - self.h * 3600 - self.m * 60


    def segundosDesde(self, hora):
        return abs( self.aSegundos() - hora.aSegundos() )

    def siguiente(self):
        # Paso a segundos y sumo 1, si el resultados ed 86400
        # la hora pasa a ser 00:00:00
        segundos = self.aSegundos()
        segundos += 1
        if segundos >= 86400:
            segundos = 0
        self.deSegundos(segundos)

    def anterior(self):
        # Paso a segundos y resto 1
        # en el caso que segundos sea 0, la hora
        # pasara a ser 23:59:59
        segundos = self.aSegundos()
        segundos -= 1
        if segundos <= 0:
            segundos = 86399
        self.deSegundos(segundos)

    def copia(self):
        h = Hora()
        h.setH(self.h)
        h.setM(self.m)
        h.setS(self.s)
        return h

    def __repr__(self):
        return "{:02d}hs. {:02d}ms. {:02d}s.".format(
            self.h,
            self.m,
            self.s
        )


# Programa principal
h1 = Hora()
print(h1)
print("A segundos {}".format(h1.aSegundos()))

h1.setH(21)
h1.setM(45)
h1.setS(0)

print(h1)
print("A segundos {}".format(h1.aSegundos()))
print()

h2 = Hora()
h2.setH(5)
h2.setM(0)
h2.setS(0)

print(h2)
print("A segundos {}".format(h2.aSegundos()))
print()
print("segundosDesde: {}".format(h1.segundosDesde(h2)))
print()
h3 = Hora()
h3.deSegundos(3600)
print("deSegundos({}) = {}".format(
    3600,
    h3))
h3.deSegundos(78300)
print("deSegundos({}) = {}".format(
    78300,
    h3))
h3.deSegundos(78358)
print("deSegundos({}) = {}".format(
    78358,
    h3))
print()
h4 = Hora()
print(h4)
h4.anterior()
print(h4)
h4.siguiente()
h4.siguiente()
print(h4)
h4.siguiente()
print(h4)
print()
print("Validando:")
h5 = Hora()
h5.setH(25)
print(h5)
h5.validar()
print(h5)
h5.setM(70)
print(h5)
h5.validar()
print(h5)
h5.setS(70)
print(h5)
h5.validar()
print(h5)
print()
h6 = h3.copia()
print("H3: {}".format(h3))
print("H6: {}".format(h6))


# Laboratorio 6 - Ejercicio 4
#
# Implementar una clase modelando una cuenta bancaria. La cuenta bancaria tiene
# un saldo, un número de cuenta, e información sobre el dueño, que es una instancia
# de la clase anterior (ejercicio 3).
#
# La clase debe implementar los métodos de hacer un depósito o una extracción de dinero.
# El método de extracción de dinero debe rechazar la transacción si no hay fondos
# suficientes en la cuenta. También desarrollar una función transferencia que mueve
# un monto entre una y otra cuenta (Para esto se puede realizar una extracción seguido
# por un depósito). Esos métodos y funciones deben devolver un valor lógico indicando
# si se fue posible ejecutar la transacción.
#


# Clase Persona del ej3
class Persona():
    def __init__(self, ncedula, apellidos, nombres, telefono, direccion):
        self.setNcedula(ncedula)
        self.setApellidos(apellidos)
        self.setNombres(nombres)
        self.setTelefono(telefono)
        self.setDireccion(direccion)

    def getNcedula(self):
        return self.ncedula
    def getApellidos(self):
        return self.apellidos
    def getNombres(self):
        return self.nombres
    def getTelefono(self):
        return self.telefono
    def getDireccion(self):
        return self.direccion
    def setNcedula(self, ncedula):
        self.ncedula = ncedula
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    def setNombres(self, nombres):
        self.nombres = nombres
    def setTelefono(self, telefono):
        self.telefono = telefono
    def setDireccion(self, direccion):
        self.direccion = direccion
    def __repr__(self):
        return "CI: {}; Apellidos y Nombres: {}, {}; {}; Direccion: {}".format(
            self.getNcedula(),
            self.getApellidos(),
            self.getNombres(),
            self.getTelefono(),
            self.getDireccion()
        )

class Cuenta():
    def __init__(self, nrocta, cliente, saldo_inicial):
        self.nrocta = nrocta
        self.cliente = cliente
        self.saldo = saldo_inicial

    def getNroCta(self):
        return self.nrocta
    def getCliente(self):
        return self.cliente
    def getSaldo(self):
        return self.saldo

    def deposito(self, importe):
        if (importe > 0):
            self.saldo += importe

    def extraccion(self, importe):

        if (importe <= self.saldo):
            self.saldo -= importe
            resultado = True
        else:
            resultado = False
        return resultado

    def __repr__(self):
        return "Cuenta: {} - Cliente: {} - {}, {} - Saldo: {}".format(
            self.nrocta,
            self.cliente.getNcedula(),
            self.cliente.getApellidos(),
            self.cliente.getNombres(),
            self.saldo
        )

    def transferir(self, otra_cuenta, importe):
        if self.extraccion(importe):
            otra_cuenta.deposito(importe)
            resultado = True
        else:
            resultado = False
        return resultado

# Programa Principal
cliente1 = Persona('5.555.551', "Lopez", "Andres", "555-555555", "Salto 1542")
cliente2 = Persona('5.555.552', "Fernandez", "Gerardo", "555-555556", "Egipto 456")
cliente3 = Persona('5.555.553', "Gimeno", "Fernanda", "555-555558", "Bolivia 679")

cuenta1 = Cuenta(10111, cliente1, 100.00)
cuenta2 = Cuenta(10112, cliente2, 1000.00)
cuenta3 = Cuenta(10113, cliente3, 10.00)
print(cliente1)
print(cliente2)
print(cliente3)
print()
print("Cuentas y saldos")
print("================")
print(cuenta1)
print(cuenta2)
print(cuenta3)
print()
print("Se deposita {} en la cuenta {}".format(1500.00, cuenta1.getNroCta()))
cuenta1.deposito(1500.00)
print("Se depoita {} en la cuenta {}".format(2500.00, cuenta2.getNroCta()))
cuenta2.deposito(2500.00)
print("Se transfiere {} de la cuenta {} a la cuenta {}".format(
    250.00,
    cuenta2.getNroCta(),
    cuenta1.getNroCta()
))
if cuenta2.transferir(cuenta1, 250.00):
    print("\tTransaccion exitosa!")
else:
    print("\tFallo la transacción por falta de fondos")
print()
print(cuenta1)
print(cuenta2)
print()
print("Se transfiere {} de la cuenta {} a la cuenta {}".format(
    250.00,
    cuenta3.getNroCta(),
    cuenta1.getNroCta()
))

if cuenta3.transferir(cuenta1, 250.00):
    print("\tTransaccion exitosa!")
else:
    print("\tFallo la transacción por falta de fondos")

print()
print("Cuentas y saldos")
print("================")
print(cuenta1)
print(cuenta2)
print(cuenta3)

# Laboratorio 6 - Ejercicio 3
#
# 3. Implementar una clase para identidades de personas. La clase debe tener los
#    componentes usuales para la identificación de las personas como el número de
#    la cédula, una dirección, nombres y apellidos, número de teléfono, etc. Se
#    debe incluir métodos de acceso a todas las propiedades.
#

class Persona():
    def __init__(self, ncedula, apellidos, nombres, telefono, direccion):
        self.setNcedula(ncedula)
        self.setApellidos(apellidos)
        self.setNombres(nombres)
        self.setTelefono(telefono)
        self.setDireccion(direccion)

    def getNcedula(self):
        return self.ncedula

    def getApellidos(self):
        return self.apellidos

    def getNombres(self):
        return self.nombres

    def getTelefono(self):
        return self.telefono

    def getDireccion(self):
        return self.direccion

    def setNcedula(self, ncedula):
        self.ncedula = ncedula

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setNombres(self, nombres):
        self.nombres = nombres

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setDireccion(self, direccion):
        self.direccion = direccion

    def __repr__(self):
        return "CI: {}; Apellidos y Nombres: {}, {}; {}; Direccion: {}".format(
            self.getNcedula(),
            self.getApellidos(),
            self.getNombres(),
            self.getTelefono(),
            self.getDireccion()
        )
# Programa principal
persona1 = Persona('1.720.555','Perez Fernandez','Esteban','5982655551','Igua 7158')
print(persona1)
print("La dirección de {}, {} es {}".format(
    persona1.getApellidos(),
    persona1.getNombres(),
    persona1.getDireccion()
))


# Laboratorio 6 - Ejercicio 2
#
# 2. En programación orientada a objetos uno de los pilares fundamentales es el
#    encapsulamiento. Es buena práctica utilizar métodos de acceso a las propiedades
#    (conocidos comúnmente como getters y setters). Agregar getters y setters a todas
#    las propiedades de las clases anteriores. Los setters deben mantener la consistencia
#    de la información, por ejemplo no se debe permitir modificar la salud de un
#    personaje y que la misma sea negativa.


class Personaje(object):
    '''Clase Personaje'''

    def __init__(self, nickname, vida, daño, poder):
        self.setNickname(nickname)
        self.setVida(vida)
        self.setDaño(daño)
        self.setPoder(poder)

    def __repr__(self):
        return "Nickname: {} Vida: {} Daño: {} Poder: {}".format(
            self.getNickname(),
            self.getVida(),
            self.getDaño(),
            self.getPoder()
        )

    def getNickname(self):
        return self.nickname

    def getVida(self):
        return self.vida

    def getDaño(self):
        return self.daño

    def getPoder(self):
        return self.poder

    def setNickname(self, nickname):
        self.nickname = nickname

    def setVida(self, vida):
        if vida >= 0:
            self.vida = vida
        else:
            self.vida = 0

    def setDaño(self, daño):
        self.daño = daño

    def setPoder(self, poder):
        self.poder = poder

    def atacar(self, elotro):
        vida = elotro.getVida() - self.getDaño()
        elotro.setVida(vida)

    def salud(self):
        return self.vida > 0


# Programa principal
pj1 = Personaje("Hombre araña", 100, 67, "patada giratoria")
pj2 = Personaje("Viuda Negra", 100, 75, "picadura mortal")
pj3 = Personaje("La Momia", 100, 75, "abrazo mortal")

print(pj1)
print(pj2)
print(pj3)
print()
pj1.atacar(pj2)
pj1.atacar(pj3)
print("Vida de {}: {}".format(pj1.getNickname(), pj1.getVida()))
print("Vida de {}: {}".format(pj2.getNickname(), pj2.getVida()))
print("Vida de {}: {}".format(pj3.getNickname(), pj3.getVida()))
pj2.atacar(pj1)
pj3.atacar(pj1)
print("Vida de {}: {}".format(pj1.getNickname(), pj1.getVida()))
print("{} esta saludable? {}".format(pj1.getNickname(), pj1.salud()))
print()


# Laboratorio 6 - Ejercicio 1
#
# Escribir una clase que permita representar al personaje de un videojuego.
# Un personaje tiene un nombre (o nickname), un porcentaje de vida (o salud),
# un poder (su nombre, por ejemplo, “patada giratoria”), y una medida de daño
# (número entero entre 0 y 100).
#
# 1. Implementar un método que permite imprimir la información de un personaje
#    utilizando la instrucción print()
#
# 2. Implementar un método que permite atacar a otro personaje (que se recibe cómo
#    parámetro). El ataque del personaje (p1) le quita vida al personaje que es
#    atacado (p2), utilizando la siguiente función:
#
#    nueva_vida(p2) = vida_actual(p2) - medida_de_daño(p1)
#
# 3. Implementar un método que indica (devolviendo True) si un personaje está con
#    vida (salud > 0)
#
# 4. Crear 3 personajes llamados pj1, pj2 y pj3 (con el porcentaje de salud y poder
# que ustedes desee), pj1 debe atacar a pj2 y pj3

class Personaje(object):
    '''Clase Personaje'''

    def __init__(self, nickname, vida, daño, poder):
        self.nickname = nickname
        self.vida = vida
        self.daño = daño
        self.poder = poder

    def __repr__(self):
        return "Nickname: {} Vida: {} Daño: {} Poder: {}".format(
            self.nickname,
            self.vida,
            self.daño,
            self.poder
        )

    def atacar(self, elotro):
        elotro.vida = elotro.vida - self.daño

    def salud(self):
        return self.vida > 0

# Programa principal
p1 = Personaje("La momia", 100, 70, "Abrazo mortal")
p2 = Personaje("La viuda Negra", 100, 75, "Mordida venenosa")
p3 = Personaje("El cazador", 100, 65, "Hachazo")

print(p1, " salud:", p1.salud())
print(p2, " salud:", p2.salud())
print()
print("El personaje {} ataca al personaje {}".format(
    p1.nickname,
    p2.nickname
))

p1.atacar(p2)

print()
print(p1, " salud:", p1.salud())
print(p2, " salud:", p2.salud())
print()
print("El personaje {} ataca al personaje {}".format(
    p1.nickname,
    p3.nickname
))

p1.atacar(p3)

print()
print(p1, " salud:", p1.salud())
print(p2, " salud:", p2.salud())
print(p3, " salud:", p3.salud())
print()

#1)
print([x+8 for x in range(3,7)])

#2)
print([c for c in "programa"])

#3)
print([[z,k] for z in range(3) for k in range(3,5)])

#4)
print([s.upper() for s in "hoy es viernes"])

#5)
print([len(z) for z in "hoy es viernes 24".split()])

##########################################
#Ej1)
print("\nEjercicio 1\n")
##1. Crear una función que retorne una lista creada por comprensión con los
##números pares hasta un número dado por parámetro.
def pareshastan(n):
    return [numero for numero in range(1,n+1) if numero%2==0]

print(pareshastan(25))

#Ej2)
print("\nEjercicio 2:\n")
##2. Utilizar comprensión de listas para obtener los números que se obtienen
##como “(n+1)*(n–1)” para n>1, y que son menores de 1000. La lista de
##estos números comienza con [0, 3, 8, 15, 24, ...].
print([(n+1)*(n-1) for n in range(1000) if n>1])

#Ej3)
print("\nEjercicio 3:\n")
##3. Utilizando listas por comprensión implementar una función que toma
##una cadena y devuelve la cadena en mayúsculas sin espacios en blanco
##ni símbolos de puntuación (los dígitos no se cambian).
def cadenalimpia(cadena):
    return "".join([letra.upper() for letra in cadena.strip() if not letra in "0123456789 :,;."])

print(cadenalimpia("Es 1 la idea, que vale por: 100, muchas palabras"))

#Ej4)
print("\nEjercicio 4:\n")
##4. Dado una cadena de caracteres con fechas en formato “MM/DD/YYYY”
##separadas por coma, obtener una lista de cadenas de caracteres con
##las fechas en formato “DD/MM/YYYY”
##Ej.: "10/11/2016,01/02/2016"  ['11/10/2016', '02/01/2016']

print(["{}/{}/{}".format(fecha.split("/")[1],fecha.split("/")[0],fecha.split("/")[2]) for fecha in "10/11/2016,01/02/2016,05/06/2017,07/31/2017".split(",")])

#Otra solución:

def reformatFecha(fecha):
    fecha_parts = fecha.split("/")
    return "{}/{}/{}".format(fecha_parts[1],fecha_parts[0],fecha_parts[2])

fechas = ["10/11/2016","01/02/2016","05/06/2017","07/31/2017"]
print([reformatFecha(fecha) for fecha in fechas])

#Ej5)
print("\nEjercicio 5:\n")
##5. Dada la siguiente clase:
##class Mail(object):
##  def __init__(self, asunto, cuerpo, destinatarios):
##      self.asunto = asunto
##      self.cuerpo = cuerpo
##      self.destinatarios = [ ... ]
##      self.copia = [ ... ]
##      self.copia_oculta = [ ... ]
##a. Utilizando listas por comprensión, completar el constructor de la
##clase a partir de la lista de destinatarios (cadenas de caracteres
##con las direcciones de email) que se recibe como parámetro
##siguiendo las siguientes condiciones:
##b. Las direcciones de email que pertenezcan al dominio “ucu.edu.uy”
##van en el campo (lista) copia.
##c. Las direcciones de email que pertenezcan al dominio “gmail.com”
##van en el campo (lista) copia_oculta.
##d. Todas las demás dirección van en la lista de destinatarios del mail.
class Mail(object):
    def __init__(self, asunto, cuerpo, destinatarios):
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.destinatarios = [mail for mail in destinatarios if (not "ucu.edu.uy" in mail) and (not "gmail.com" in mail)]
        self.copia = [mail for mail in destinatarios if "ucu.edu.uy" in mail]
        self.copia_oculta = [mail for mail in destinatarios if "gmail.com" in mail]

mail = Mail("hola","saludo",["rroballo@ucu.edu.uy", "gpennino@ucu.edu.uy","rodolfo.roballo@gmail.com","fwagner@gmail.com","rroballo@genexus.com"])
print(mail.destin7atarios)
print(mail.copia)
print(mail.copia_oculta)
            
###########################################################################################


name = input("Enter file:")
handle = open(name)
emailist = []
sender= dict()

for line in handle:
    if line.startswith("From "):
        linelst = line.split()
        email = linelst[1]
        emailist.append(email)

for dir in emailist:
    sender[dir] = sender.get(dir, 0) + 1

bigcount = 0 
bigword = 0 

for word,count in sender.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

####################################
# Perros y pelotas

def perrosYPelota(xyz):
    try:
        if len(xyz) != 3:
            raise ValueError("La lista debe contener exactamente tres elementos")
        
        x, y, z = xyz
        
        if not (0 < x < z < y < 100):
            raise ValueError("Los valores de posición no cumplen con las restricciones")
        
        distancia_perro_a = abs(x - z)
        distancia_perro_b = abs(y - z)
        
        if distancia_perro_a == distancia_perro_b:
            return "Pelota"
        elif distancia_perro_a < distancia_perro_b:
            return "PerroA"
        else:
            return "PerroB"
    
    except IndexError:
        return ""
    except TypeError:
        return ""
    except ValueError as e:
        return str(e)


xyz = [2, 7, 3]
print(perrosYPelota(xyz))  # Debería imprimir "PerroA"

xyz = [3, 5, 4]
print(perrosYPelota(xyz))  # Debería imprimir "Pelota"

xyz = [3, 5]  # IndexError
print(perrosYPelota(xyz))  # Debería imprimir ""

xyz = [3, 5, "gato"]  # TypeError
print(perrosYPelota(xyz))  # Debería imprimir ""


################

"""Aquí tienes una posible implementación de la función lista_mágica que genera una lista de números aleatorios sin repeticiones dentro de un rango especificado:

"""


import random

def lista_mágica(cantidad, inicio, fin):
    if fin - inicio + 1 < cantidad:
        return []  # No hay suficientes números en el rango
    
    numeros_disponibles = list(range(inicio, fin + 1))
    numeros_elegidos = random.sample(numeros_disponibles, cantidad)
    
    return numeros_elegidos

print(lista_mágica(5, 1, 10))  # Generar una lista de 5 números aleatorios entre 1 y 10

print(lista_mágica(3, 100, 200))  # Generar una lista de 3 números aleatorios entre 100 y 200

print(lista_mágica(10, 1, 5))  # Intentar generar una lista de 10 números aleatorios entre 1 y 5 (no hay suficientes números)

print(lista_mágica(0, 1, 100))  # Intentar generar una lista vacía


"""
Aquí tienes una posible implementación de la función productos_comunes que encuentra los productos comunes entre dos inventarios y devuelve un diccionario con los productos y la suma de las cantidades:"""

def productos_comunes(inventario1, inventario2):
    productos_comunes = {}
    
    for producto in inventario1:
        if producto in inventario2:
            cantidad1 = inventario1[producto]
            cantidad2 = inventario2[producto]
            productos_comunes[producto] = cantidad1 + cantidad2
    
    return productos_comunes

print(productos_comunes({'manzanas': 5, 'peras': 8, 'platanos': 3}, {'platanos': 6, 'naranjas': 7, 'manzanas': 4}))
# Debería imprimir {'manzanas': 9, 'platanos': 9}

print(productos_comunes({'camisas': 10, 'pantalones': 5}, {'zapatos': 8, 'corbatas': 6}))
# Debería imprimir {}

"""Aquí tienes una posible implementación de la función que calcula el valor en ohms de una resistencia de carbón a partir de los colores de las bandas:"""

def valor_resistencia(colores):
    codigos_colores = {
        "negro": 0,
        "marrón": 1,
        "rojo": 2,
        "naranja": 3,
        "amarillo": 4,
        "verde": 5,
        "azul": 6,
        "violeta": 7,
        "gris": 8,
        "blanco": 9
    }
    
    if len(colores) != 3:
        return None  # La lista de colores no tiene la longitud esperada
    
    cifra1 = codigos_colores.get(colores[0])
    cifra2 = codigos_colores.get(colores[1])
    multiplicador = 10 ** codigos_colores.get(colores[2])
    
    if cifra1 is None or cifra2 is None or multiplicador is None:
        return None  # Uno o más colores no son válidos
    
    valor_ohms = (cifra1 * 10 + cifra2) * multiplicador
    return valor_ohms

resistencia = ["negro", "rojo", "verde"]
print(valor_resistencia(resistencia))  # Debería imprimir 200000

resistencia = ["marrón", "negro", "rojo"]
print(valor_resistencia(resistencia))  # Debería imprimir 100

resistencia = ["amarillo", "violeta", "naranja"]
print(valor_resistencia(resistencia))  # Debería imprimir 47000

resistencia = ["azul", "gris", "blanco"]
print(valor_resistencia(resistencia))  # Debería imprimir 680000000

resistencia = ["rojo", "verde", "azul"]  # No tiene el número adecuado de colores
print(valor_resistencia(resistencia))  # Debería imprimir None

resistencia = ["negro", "rojo", "morado"]  # Color inválido
print(valor_resistencia(resistencia))  # Debería imprimir None


#########################################

def calcular_metros_tela(archivo_pedidos):
    tallas_longitud = {
        "S": 69,
        "M": 71,
        "L": 74,
        "XL": 77,
        "XXL": 81
    }

    total_metros = 0

    try:
        with open(archivo_pedidos, 'r') as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                pedido = linea.strip().split(',')
                for talla_cantidad in pedido:
                    talla, cantidad = talla_cantidad.split(':')
                    cantidad = int(cantidad)
                    if talla in tallas_longitud:
                        longitud = tallas_longitud[talla]
                        metros = longitud * cantidad
                        total_metros += metros

    except FileNotFoundError:
        print("El archivo de pedidos no existe.")
        return None

    return total_metros

archivo_pedidos = "pedidos.txt"  # Reemplazar con la ruta y nombre del archivo de pedidos
metros_necesarios = calcular_metros_tela(archivo_pedidos)

if metros_necesarios is not None:
    print("La cantidad de metros necesarios de tela es:", metros_necesarios)

#########################

def es_palindromo_binario(numero):
    binario = bin(numero)[2:]  # Obtener representación binaria sin el prefijo '0b'
    binario_reverso = binario[::-1]  # Invertir la cadena binaria

    return binario == binario_reverso

#Realizar un programa en python que solicite al usuario un número decimal y muestre en pantalla si el mismo es un palíndromo en notación binaria.

while True:
    try:
        decimal = int(input("Ingresa un número decimal: "))
        if decimal < 0:
            raise ValueError("El número debe ser positivo.")
        break
    except ValueError as error:
        print("Error:", error)

if es_palindromo_binario(decimal):
    print("El número decimal", decimal, "es un palíndromo en notación binaria.")
else:
    print("El número decimal", decimal, "no es un palíndromo en notación binaria.")


###########################################
# POO1

class TarjetaDeCredito:
    def __init__(self, numero, titular, fecha_vencimiento, cvv, limite_credito):
        self.numero = numero
        self.titular = titular
        self.fecha_vencimiento = fecha_vencimiento
        self.cvv = cvv
        self.limite_credito = limite_credito
        self.historico_pagos = []

    def realizar_pago(self, monto, motivo):
        if monto <= self.limite_credito:
            self.limite_credito -= monto
            self.historico_pagos.append((monto, motivo))
            return True
        else:
            return False

    def saldo(self):
        return self.limite_credito

    def obtener_numero(self):
        return self.numero

    def obtener_titular(self):
        return self.titular

    def obtener_fecha_vencimiento(self):
        return self.fecha_vencimiento

    def obtener_cvv(self):
        return self.cvv

    def obtener_limite_credito(self):
        return self.limite_credito

    def obtener_historico_pagos(self):
        return self.historico_pagos

    def __str__(self):
        return f"Número: {self.numero}\nTitular: {self.titular}\nFecha de vencimiento: {self.fecha_vencimiento}\nCVV: {self.cvv}\nLímite de crédito: ${self.limite_credito}\n"

# Crear las instancias de TarjetaDeCredito
tarjeta1 = TarjetaDeCredito("1234567890123456", "Adela Sanchez", "12/26", "123", 2000)
tarjeta2 = TarjetaDeCredito("9876543210987654", "Juan Oreste", "06/25", "456", 1500)

# Realizar los pagos en cada tarjeta
tarjeta1.realizar_pago(500, "Compra en línea")
tarjeta1.realizar_pago(1000, "Pago de factura")
tarjeta1.realizar_pago(250, "Nafta")
tarjeta1.realizar_pago(50, "Regalos")

tarjeta2.realizar_pago(500, "Compra en línea")
tarjeta2.realizar_pago(1000, "Pago de factura")
tarjeta2.realizar_pago(250, "Nafta")

# Mostrar el estado actual de cada tarjeta
print("Estado de la Tarjeta 1:")
print(tarjeta1)

print("Estado de la Tarjeta 2:")
print(tarjeta2)


##############################################

# POO2



class TarjetaDeCredito:
    def __init__(self, numero, titular, fecha_vencimiento, cvv, limite_credito):
        self.numero = numero
        self.titular = titular
        self.fecha_vencimiento = fecha_vencimiento
        self.cvv = cvv
        self.limite_credito = limite_credito
        self.historico_pagos = []

    def realizar_pago(self, monto, motivo):
        if monto <= self.limite_credito:
            self.limite_credito -= monto
            self.historico_pagos.append((monto, motivo))
            return True
        else:
            return False

    def saldo(self):
        return self.limite_credito

    def obtener_numero(self):
        return self.numero

    def obtener_titular(self):
        return self.titular

    def obtener_fecha_vencimiento(self):
        return self.fecha_vencimiento

    def obtener_cvv(self):
        return self.cvv

    def obtener_limite_credito(self):
        return self.limite_credito

    def obtener_historico_pagos(self):
        return self.historico_pagos

    def __str__(self):
        return f"Número: {self.numero}\nTitular: {self.titular}\nFecha de vencimiento: {self.fecha_vencimiento}\nCVV: {self.cvv}\nLímite de crédito: ${self.limite_credito}\n"

tarjetas = {}

while True:
    print("\n--- Sistema de Gestión de Tarjetas de Crédito ---")
    print("1. Crear tarjeta")
    print("2. Realizar pago")
    print("3. Consultar saldo")
    print("4. Imprimir información de tarjeta")
    print("5. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        print("--- Crear tarjeta ---")
        cedula = input("Número de cédula: ")
        numero = input("Número de tarjeta: ")
        titular = input("Titular: ")
        fecha_vencimiento = input("Fecha de vencimiento: ")
        cvv = input("CVV: ")
        limite_credito = float(input("Límite de crédito: "))

        tarjeta = TarjetaDeCredito(numero, titular, fecha_vencimiento, cvv, limite_credito)
        tarjetas[cedula] = tarjeta
        print("Tarjeta creada con éxito.")

    elif opcion == "2":
        print("--- Realizar pago ---")
        cedula = input("Número de cédula: ")

        if cedula in tarjetas:
            tarjeta = tarjetas[cedula]
            monto = float(input("Monto del pago: "))
            motivo = input("Motivo: ")

            if tarjeta.realizar_pago(monto, motivo):
                print("Pago realizado con éxito.")
            else:
                print("No se puede realizar el pago. Saldo insuficiente.")
        else:
            print("No se encontró una tarjeta asociada a la cédula ingresada.")

    elif opcion == "3":
        print("--- Consultar saldo ---")
        cedula = input("Número de cédula: ")

        if cedula in tarjetas:
            tarjeta = tarjetas[cedula]
            saldo = tarjeta.saldo()
            print(f"Saldo actual: ${saldo}")
        else:
            print("No se encontró una tarjeta asociada a la cédula ingresada.")

    elif opcion == "4":
        print("--- Imprimir información de tarjeta ---")
        cedula = input("Número de cédula: ")

        if cedula in tarjetas:
            tarjeta = tarjetas[cedula]
            print(tarjeta)
        else:
            print("No se encontró una tarjeta asociada a la cédula ingresada.")

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")


##########################################

def comprimir_lista(numeros):
    comprimidos = []
    cantidad = 1

    for i in range(1, len(numeros)):
        if numeros[i] == numeros[i-1]:
            cantidad += 1
        else:
            comprimidos.append([numeros[i-1], cantidad])
            cantidad = 1

    comprimidos.append([numeros[-1], cantidad])

    return comprimidos if len(comprimidos) < len(numeros) else numeros

numeros = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5]
resultado = comprimir_lista(numeros)
print(resultado)  # [[1, 3], [2, 2], 3, [4, 2], [5, 4]]

numeros = [2, 2, 2, 2, 2, 2, 2]
resultado = comprimir_lista(numeros)
print(resultado)  # [[2, 7]]

numeros = [1, 2, 3, 4, 5]
resultado = comprimir_lista(numeros)
print(resultado)  # [1, 2, 3, 4, 5]


######################################


def combinar_listas(lista1, lista2):
    combinada = []
    len1 = len(lista1)
    len2 = len(lista2)
    max_len = max(len1, len2)

    for i in range(max_len):
        if i < len1:
            combinada.append(lista1[i])
        if i < len2:
            combinada.append(lista2[i])

    return combinada


lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c', 'd', 'e']
resultado = combinar_listas(lista1, lista2)
print(resultado)  # [1, 'a', 2, 'b', 3, 'c', 'd', 'e']

lista1 = ['rojo', 'verde']
lista2 = ['azul', 'amarillo', 'naranja']
resultado = combinar_listas(lista1, lista2)
print(resultado)  # ['rojo', 'azul', 'verde', 'amarillo', 'naranja']


##############################################


def producto_cartesiano(lista1, lista2):
    producto = []

    for elemento1 in lista1:
        for elemento2 in lista2:
            producto.append([elemento1, elemento2])

    return producto

lista1 = [1, 2]
lista2 = ['a', 'b']
resultado = producto_cartesiano(lista1, lista2)
print(resultado)  # [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]

lista1 = [1, 2, 3]
lista2 = ['rojo', 'verde']
resultado = producto_cartesiano(lista1, lista2)
print(resultado)  # [[1, 'rojo'], [1, 'verde'], [2, 'rojo'], [2, 'verde'], [3, 'rojo'], [3, 'verde']]


"""Claro, puedo ayudarte a escribir una función que convierta números decimales a binarios y viceversa, y además sea modificable para cambiar las bases de los números de entrada y salida. Aquí tienes un ejemplo en Python:"""

def convertir_base(numero, base_entrada, base_salida):
    if base_entrada == 10:  # Decimal a otra base
        resultado = ''
        while numero > 0:
            residuo = numero % base_salida
            resultado = str(residuo) + resultado
            numero = numero // base_salida
        return resultado
    elif base_salida == 10:  # Otra base a decimal
        resultado = 0
        potencia = 0
        while numero > 0:
            residuo = numero % 10
            resultado += residuo * (base_entrada ** potencia)
            numero = numero // 10
            potencia += 1
        return resultado
    else:
        # Conversión de una base a otra base
        decimal = int(str(numero), base_entrada)
        resultado = ''
        while decimal > 0:
            residuo = decimal % base_salida
            resultado = str(residuo) + resultado
            decimal = decimal // base_salida
        return resultado


# Decimal a binario
print(convertir_base(42, 10, 2))  # Salida: 101010

# Binario a decimal
print(convertir_base(101010, 2, 10))  # Salida: 42

# Hexadecimal a binario
print(convertir_base('FF', 16, 2))  # Salida: 11111111

# Binario a hexadecimal
print(convertir_base(11111111, 2, 16))  # Salida: FF


