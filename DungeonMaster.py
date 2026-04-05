pref = ["*", "&", "#", "!"]

def verificar(c, base):
    if base == 2:
        return c in "01"
    elif base == 8:
        return c in "01234567"
    elif base == 10:
        return c in "0123456789"
    elif base == 16:
        return c in "0123456789ABCDEFabcdef"
    return False

def to_text(pref):
    match pref:
        case "*":
            return "Binario"
        case "&":
            return "Octal"
        case "#":
            return "Decimal"
        case "!":
            return "Hexadecimal"

def lectura():
    with open("notas_dm.txt", "r") as file:
        data = file.read()
    i = 0
    valores = []
    while i < len(data):
        if data[i] in pref:
            prefijo = data[i]
            match prefijo:
                case "*":
                    base = 2
                case "&":
                    base = 8
                case "#":
                    base = 10
                case "!":
                    base = 16
            i += 1
            numero = ""
            while i < len(data) and verificar(data[i], base):
                numero += data[i]
                i += 1
            if numero != "":
                valores.append((prefijo, numero, base))
        else:
            i += 1
    return valores

def hex_helper(c):
    match c:
        case 'A' | 'a':
            return 10
        case 'B' | 'b':
            return 11
        case 'C' | 'c':
            return 12
        case 'D' | 'd':
            return 13
        case 'E' | 'e':
            return 14
        case 'F' | 'f':
            return 15
        case _:
            return int(c)

def reverse_hex_helper(n):
    if n < 10:
        return str(n)

    match n:
        case 10:
            return "A"
        case 11:
            return "B"
        case 12:
            return "C"
        case 13:
            return "D"
        case 14:
            return "E"
        case 15:
            return "F"
        
# forma de la lista [("*", "1010", 2), ("&", "17", 8), ("#", "255", 10), ("!", "1A3F", 16)]

def to_decimal(numero, base):
    print("\nNumero: ", numero, "\n")
    final = len(numero) - 1
    result = 0
    cont = 0
    match base:
        case 2:
            while final >= 0:
                result += int(numero[final]) * (2 ** cont)
                cont += 1
                final -= 1
            return result
        case 8:
            while final >= 0:
                result += int(numero[final]) * (8 ** cont)
                cont += 1
                final -= 1
            return result
        case 10:
            return int(numero)
        case 16:
            while final >= 0:
                result += hex_helper(numero[final]) * (16 ** cont)
                cont += 1
                final -= 1
            return result
# no listos
def to_binary(numero, base):
    result=""
    match base:
        case 2:
            return numero
        case 8:
            result = to_binary(str(to_decimal(numero,base)),10)
            print(result)
            return result
        case 10:
            while int(numero)//2 >= 1:
                resto=int(numero)%2
                if resto == 1:
                    result = result + "1"
                elif resto == 0:
                    result = result + "0"
                numero = int(numero)//2
            resto = int(numero)%2
            result = result + str(resto)
            return result[::-1]
        case 16:
            result = to_binary(str(to_decimal(numero,base)),10)[::-1]
            if (len(result)%4 != 0):
                faltantes=4-(len(result)%4)
                while (faltantes>0):
                    result+="0"
                    faltantes-=1
            return result[::-1]
        
def to_hex(numero, base):
    if base != 10:
        dec = to_decimal(numero, base)
    else:
        dec = int(numero)

    if dec == 0:
        return "0"
    
    result=""
    while dec > 0:
        resto = dec % 16
        char = reverse_hex_helper(resto)
        result = char + result
        dec = dec // 16

    return result

def to_octal(numero, base):

    if base != 10:
        dec = to_decimal(numero, base)
    else:
        dec = int(numero)
        
    if dec == 0:
        return "0"

    result = ""
    while dec > 0:
        resto = dec % 8
        result = str(resto) + result
        dec = dec // 8
        
    return result

def main():
    print("--- DECODIFICADOR DE NOTAS ---\n")
    # n=input("TO BINARY\n Manda un NUMERO para transformarlo a OCTAL: ")
    # base=input("Ingresa la base papu: ")
    # print(to_octal(n,int(base)))
    
    base = int(input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): "))
    if(base not in [2, 8, 10, 16]):
        return
    print("\n[+] Procesando archivo: notas_dm.txt...\n[!] Filtrando ruido místico (valores fuera de rango ASCII)...\n")
    print(f"LISTA DE VALORES EXTRAÍDOS (Base {base}):")
    print("-------------------------------------------------")
    #FUNCIONES
    valores = lectura()
    print(" \n\nEstos son los valores: ", valores)
    salida = []
    for pref, num, aux in valores:
        match base:
            case 2:
                salida.append((pref, to_binary(num, aux), num, to_text(pref)))
            case 8:
                salida.append((pref, to_octal(num, aux), num, to_text(pref)))
            case 10:
                salida.append((pref, to_decimal(num, aux), num, to_text(pref)))
            case 16:
                salida.append((pref, to_hex(num, aux), num, to_text(pref)))

    i = 1
    for pref, num, org, aux in salida:
        print(f"VALOR {i}: {num} (Original: {aux} {pref}{org})")
        i += 1
    print("-------------------------------------------------\n")
    print("MENSAJE DECODIFICADO:")
    # MENSAJE
    print("\n[Proceso finalizado con éxito]")

main()