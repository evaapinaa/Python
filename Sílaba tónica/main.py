def obtenerSilabaTonica(lista_silabas): 
    #Si una palabra sin tilde termina en vocal, o en las letras 's' o 'n', tiene dos o más sílabas,
    #la penúltima sílaba es la tónica. Por ejemplo: Examen
    if len(lista_silabas) >= 2 and (lista_silabas[-1][-1] in 'aeiou' or lista_silabas[-1][-1] in 'sn'):
        return -2
     # Si una palabra sin tilde termina con una consonante distinta de 's' o 'n', la última sílaba es la tónica.
    else:
        return -1


def buscarVocalTonica(silaba):
    # Si una palabra sin tilde termina con una consonante distinta de 's' o 'n', la última sílaba
    # es la tónica. Por ejemplo: ababol
    # En los diptongos la vocal tónica es la abierta o la segunda cerrada.
    # En los triptongos la vocal tónica es la central.
    vocales_abiertas = "aeo"
    vocales_cerradas = "iu"
    
    for i in range(len(silaba)):
        # Si encontramos una vocal abierta en la sílaba
        if silaba[i] in vocales_abiertas:
            # Reemplazamos la vocal con su versión en mayúscula en la misma posición
            return silaba[:i] + silaba[i].upper() + silaba[i+1:]
        # Si encontramos una vocal cerrada en la sílaba
        elif silaba[i] in vocales_cerradas:
            # Reemplazamos la vocal con su versión en mayúscula en la misma posición
            return silaba[:i] + silaba[i].upper() + silaba[i+1:]
    
    # Si no se encuentra ninguna vocal abierta o cerrada, se considera la última vocal como tónica
    return silaba[:-1] + silaba[-1].upper()


def entonacion(lista_silabas):

    Tildada = False

    for i in range(len(lista_silabas)):
        silaba = lista_silabas[i]
        for caracter in silaba:
            if caracter in 'á,é,í,ó,ú':
                
                Tildada = True

                if caracter == 'á':
                    lista_silabas[i] = silaba.replace(caracter, 'A')
                    
                elif caracter == 'é':
                    lista_silabas[i] = silaba.replace(caracter, 'E')

                elif caracter == 'í':
                    lista_silabas[i] = silaba.replace(caracter, 'I')

                elif caracter == 'ó':
                    lista_silabas[i] = silaba.replace(caracter, 'O')

                elif caracter == 'ú':
                    lista_silabas[i] = silaba.replace(caracter, 'U')


    # En caso de que no tenga tilde
    if not Tildada:
        
        sT = obtenerSilabaTonica(lista_silabas) # La función devuelve el índice de la sílaba tónica
        lista_silabas[sT] = buscarVocalTonica(lista_silabas[sT])

    return lista_silabas


print(entonacion(["ra", "tón"]))
print(entonacion(["ra", "ta"]))
print(entonacion(["fur", "gón"]))
print(entonacion(["man", "za", "na"]))
print(entonacion(["pa", "to"]))
print(entonacion(["ex", "a", "men"]))