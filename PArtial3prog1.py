ingredientes = {
    "carne": 100,
    "pollo": 90,
    "espinaca": 80,
    "pan": 40,
    "lechuga": 10,
    "tomate": 10,
    "cebolla": 10,
    "mozzarella": 30,
    "huevo": 40
}

def calcular_precio_pedido(pedido):
    total = 0
    vegetariano = True
    
    for ingrediente in pedido:
        if ingrediente in ingredientes:
            total += ingredientes[ingrediente]
            if ingrediente == "carne" or ingrediente == "pollo":
                vegetariano = False
        else:
            total = 0
            break
    
    return total, vegetariano

def procesar_archivo_pedidos(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            pedidos = archivo.readlines()
        
        for i, pedido in enumerate(pedidos):
            ingredientes_pedido = pedido.strip().split(",")
            precio, vegetariano = calcular_precio_pedido(ingredientes_pedido)
            
            if precio == 0:
                print(f"Pedido {i+1}: Faltan Ingredientes - no se puede completar el pedido")
            else:
                if vegetariano:
                    print(f"Pedido {i+1}: ${precio:.2f} Vegetariano")
                else:
                    print(f"Pedido {i+1}: ${precio:.2f}")
    
    except FileNotFoundError:
        print("El archivo de pedidos no existe.")


procesar_archivo_pedidos("hamburguesas.txt")

#ejercicio 3

def calcular_deficit_hidrico(cultivos):
    deficit_hidrico = {} #deberemos crear un diccionario vacío donde almacenaremos los pares clave valor de los cultivos y su déficit
    for cultivo, demanda, precipitacion in cultivos.items():  #en los items del archivo hay que analizar los valores de cultivo, demanda, precipitacion
        if precipitacion < demanda: #esto está bastante claro
            deficit_hidrico[cultivo] = demanda - precipitacion
        else:
            deficit_hidrico[cultivo] = 0
    return deficit_hidrico

def grabar(deficit_hidrico):
    with open("resultados_deficit_hidrico.txt", "w") as file:
        for cultivo, deficit in deficit_hidrico.items():
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