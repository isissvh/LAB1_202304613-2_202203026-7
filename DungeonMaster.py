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

# forma de la lista [("*", "1010", 2), ("&", "17", 8), ("#", "255", 10), ("!", "1A3F", 16)]

def to_decimal(numero, base):
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

def to_binary(numero, base):
    return
def to_hex(numero, base):
    return
def to_octal(numero, base):
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
            return int(numero)
        case 10:
            resguardo = numero
            while num > 0:
                if num % 8 == 0:
                    
                else:
                    num = num // 8
            return result

        case 16:
            while final >= 0:
                result += hex_helper(numero[final]) * (16 ** cont)
                cont += 1
                final -= 1
            return result

def main():
    print("--- DECODIFICADOR DE NOTAS ---\n")
    base = int(input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): "))
    if(base not in [2, 8, 10, 16]):
        return
    print("\n[+] Procesando archivo: notas_dm.txt...\n[!] Filtrando ruido místico (valores fuera de rango ASCII)...\n")
    print(f"LISTA DE VALORES EXTRAÍDOS (Base {base}):")
    print("-------------------------------------------------")
    #FUNCIONES
    valores = lectura()
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