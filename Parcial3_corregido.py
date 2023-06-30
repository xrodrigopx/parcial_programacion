ingredientes = {
"carne": 100,
"pollo": 90,
"espinaca": 80, #medio cara la espinaca
"pan": 40,
"lechuga": 10,
"tomate": 10, 
"cebolla": 10,
"mozzarella": 30,
"huevo": 40
}

#ahora vamos a ver la lógica detrás del programa, para luego trabajar con el archivo en base a esta lógica
def calcular_precio_pedido(pedido):
    total = 0 #tomemos el valos inicial del precio como 0 si no tenemos ingredientes
    vegetariano = True #por default, si el menú tiene solo un elemento que no es carne o varios, será vegetariano
    
    for ingrediente in pedido: #entonces, cuando señalemos los ingredientes del menú, armaremos una listita
        if ingrediente in ingredientes: #recorreremos la lista
            total += ingredientes[ingrediente] #habiendo agregado los elementos
            if ingrediente == "carne" or ingrediente == "pollo": #pero si uno es carne o pollo
                vegetariano = False #ya no será vegetariano
        else:
            total = 0 #si no ponemos nada
            break #se romperá el programa
    
    return total, vegetariano #al final, devolveremos el total del menú

#ahora vamos con el archivo
def procesar_archivo_pedidos(nombre_archivo):
    try: #intentaremos abrir el archivo y hacer lo siguiente:
        with open(nombre_archivo, 'r') as archivo: #leer el archivo de ingredientes
            pedidos = archivo.readlines() #con esta pequeña función
        
        for i, pedido in enumerate(pedidos, 1): #en la lista de ingedientes, le asignaremos un valor único a cada uno
            ingredientes_pedido = pedido.strip().split(",") #separaremos los ingredientes uno por uno
            precio, vegetariano = calcular_precio_pedido(ingredientes_pedido) #para luego, en base al precio y aptitud del menú
            #imprimiremos si el pedido es válido
            if precio == 0:
                print(f"Pedido {i+1}: Faltan Ingredientes - no se puede completar el pedido")
            else: #si es vegetariano
                if vegetariano:
                    print(f"Pedido {i+1}: {precio} Vegetariano")
                else: #y el precio final
                    print(f"Pedido {i+1}: {precio}")
    
    except FileNotFoundError: #al final, si el archivo tiene cualquier cosa adentro, tiraremos un lindo error
        print("El archivo de pedidos no existe.")

#vamso a llamar la función a ver
procesar_archivo_pedidos("archivo_de_pedidos.txt") 


###############################################################################################################


def calcular_deficit_hidrico(cultivos):
    deficit_hidrico = {}
    for cultivo, valores in cultivos.items():
        demanda = valores[0]
        precipitacion = valores[1]
        if precipitacion < demanda:
            deficit_hidrico[cultivo] = demanda - precipitacion
        else:
            deficit_hidrico[cultivo] = 0
    return deficit_hidrico

def grabar(deficit_hidrico):
    with open("resultados_deficit_hidrico.txt", "w") as file:
        for cultivo in deficit_hidrico.keys():
            deficit = int(deficit_hidrico[cultivo])
            if deficit > 0:
                file.write(f"{cultivo},Si,{deficit}\n")
            else:
                file.write(f"{cultivo},No,0\n")

cultivos = {
    'Maiz': [600, 450],
    'Trigo': [450, 350],
    'Arroz': [800, 900],
    'Soja': [550, 400]
}

deficit_hidrico = calcular_deficit_hidrico(cultivos)
grabar(deficit_hidrico)


###############################################################################



def clase_ip(dir_ip):
    try:

        
        # lo que estoy por hacer no le va a gustar
        octetos = dir_ip.split('.')
        
        # pero si no lo hago, no entrego nada, sepa entender
        binario = [bin(int(octeto))[2:].zfill(8) for octeto in octetos]
        
        # hay que definir como empieza la ip entonces con el .startswith()
        primer_octeto = binario[0]
        if primer_octeto.startswith('0'):
            return 'A'
        elif primer_octeto.startswith('10'):
            return 'B'
        elif primer_octeto.startswith('110'):
            return 'C'
        elif primer_octeto.startswith('1110'):
            return 'D'
        elif primer_octeto.startswith('1111'):
            return 'E'
        else:
            return 'No válida'
    except ValueError:
        return 'No válida'

dir_ip = "192.168.2.1"
clase = clase_ip(dir_ip)
print("La ip: " + dir_ip + " es de clase: " + clase)

