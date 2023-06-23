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