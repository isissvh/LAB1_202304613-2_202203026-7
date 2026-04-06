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

oct_bin = {
    '0': '000', '1': '001', '2': '010', '3': '011',
    '4': '100', '5': '101', '6': '110', '7': '111'
}
bin_oct = {v: k for k, v in oct_bin.items()}

bin_hex = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}
hex_bin = {v: k for k, v in bin_hex.items()}

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
                numero += data[i].upper()
                i += 1
            if numero != "":
                valores.append((prefijo, numero, base))
        else:
            i += 1
    return valores

# forma de la lista Ej: [("*", "1010", 2), ("&", "17", 8), ("#", "255", 10), ("!", "1A3F", 16)]

def hex_helper(n):
    match n:
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
            return int(n)

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
    result=""
    match base:
        case 2:
            return numero
        case 8:
            for num in numero:
                result += oct_bin[num]
            return result.lstrip('0') or '0'
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
            for num in numero:
                result += hex_bin[num]
            return result.lstrip('0') or '0'
        
def to_hex(numero, base):
    result=""
    match base:
        case 16:
            return numero
        case 10:
            dec = int(numero)
            if dec == 0:
                return "0"
            while dec > 0:
                resto = dec % 16
                char = reverse_hex_helper(resto)
                result = char + result
                dec = dec // 16
            return result
        case 8:
            complete = ""
            for num in numero:
                complete += oct_bin[num]
            if len(complete) % 4 != 0:
                complete = ("0" * (4 - len(complete) % 4)) + complete
            for i in range(0, len(complete), 4):
                segment = complete[i:i+4]
                result += bin_hex[segment]
            return result.lstrip('0') or '0'
        case 2:
            complete = numero
            if len(complete) % 4 != 0:
                complete = ("0" * (4 - len(complete) % 4)) + complete
            for i in range(0, len(complete), 4):
                segment = complete[i:i+4]
                result += bin_hex[segment]
            return result.lstrip('0') or '0'    

def to_octal(numero, base):
    result=""
    match base:
        case 16:
            complete = ""
            for num in numero:
                complete += hex_bin[num]
            if len(complete) % 3 != 0:
                complete = ("0" * (3 - len(complete) % 3)) + complete
            for i in range(0, len(complete), 3):
                segment = complete[i:i+3]
                result += bin_oct[segment]
            return result.lstrip('0') or '0'
        case 10:
            dec = int(numero)
            if dec == 0:
                return "0"
            while dec > 0:
                resto = dec % 8
                result = str(resto) + result
                dec = dec // 8
            return result
        case 8:
            return numero
        case 2:
            complete = numero
            if len(complete) % 3 != 0:
                complete = ("0" * (3 - len(complete) % 3)) + complete
            for i in range(0, len(complete), 3):
                segment = complete[i:i+3]
                result += bin_oct[segment]
            return result.lstrip('0') or '0'

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
    mensaje=""
    for pref, num, aux in valores:
        valido = to_decimal(num,aux)
        if (valido>=32 and valido<=126):
            match base:
                case 2:
                    salida.append((pref, to_binary(num, aux), num, to_text(pref)))
                case 8:
                    salida.append((pref, to_octal(num, aux), num, to_text(pref)))
                case 10:
                    salida.append((pref, to_decimal(num, aux), num, to_text(pref)))
                case 16:
                    salida.append((pref, to_hex(num, aux), num, to_text(pref)))

            mensaje += chr(valido)
            
    i = 1
    #filtrar salida
    for pref, num, org, aux in salida:
        print(f"VALOR {i}: {num} (Original: {aux} {pref}{org})")
        i += 1
    print("-------------------------------------------------\n")
    print("MENSAJE DECODIFICADO:\n")
    print(mensaje)
    print("\n[Proceso finalizado con éxito]")

if __name__ == "__main__":
    main()