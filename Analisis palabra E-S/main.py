def analisislongitud(word):
    return len(word.strip())


def analisismayuscula(word):
    mayus = False
    for letra in word:
        if letra == letra.upper():
            mayus = True
            break
    return mayus


while True:
    print("Opcion 1 -> Analisis de una palabra a introducir")
    print("Opcion 2 -> Analisis de las palabras de un fichero")
    print("Opcion 3 -> Pulse Enter para finalizar")

    opcion = input("Introduzca la opcion que desee: ")

    if not opcion:
        break

    elif opcion == '1':

        pUsuario = input("Introduzca una palabra: ")

        while pUsuario:
            print(f"La longitud de la palabra '{pUsuario}' es de {analisislongitud(pUsuario)} letras.", end=' ')

            if analisismayuscula(pUsuario):
                print("Contiene alguna mayuscula.")
            else:
                print("No contiene ninguna mayuscula.")
            break

    elif opcion == '2':
        nombreFile = input("Introduzca el nombre del fichero: ")

        try:
            archivo = open(file=nombreFile)

        except FileNotFoundError:
            print("No se encuentra el fichero. Asegurese que lo ha escrito correctamente y vuelva a intentarlo")

        else:
            while True:
                lineas = archivo.readlines()
                archivo2 = open('salida.csv', 'w')
                print("Palabra;Longitud;Mayuscula", file=archivo2)

                for linea in lineas:
                    if linea != '\n':
                        palabra = linea.strip()
                        longitud = analisislongitud(palabra)
                        mayuscula = analisismayuscula(palabra)
                        print(f"{palabra};{longitud};{mayuscula}", file=archivo2)

                if not lineas:
                    break

                print("Guardando el fichero 'salida.csv'...")
                print("Finalizado")
