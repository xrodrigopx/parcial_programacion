def clase_ip(dir_ip):
    try:
    
        if decimal == 0:
            return "0"
        
        binario = ""
        
        while decimal > 0:
            bit = decimal % 2
            binario = str(bit) + binario
            decimal = decimal // 2
            
   
        # Determinar la clase basada en el primer octeto
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
