
contenido = list()

with open('../../../../resource/doc/bares.txt', 'r') as archivo:
    for linea in archivo:
        columnas = linea.split(' ')
        columnas[0] = ''
        contenido.append(' '.join(columnas)+'\n')

with open('../../../../resource/doc/bares.txt', 'w') as archivo:
    archivo.writelines(contenido)

def modificar_dato(ruta, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta, 'r+') as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila-1].split(' ')
            columnas[columna] = nuevo_dato
            contenido[fila-1] = ' '.join(columnas)+ '\n'
    with open(ruta, 'w') as archivo:
        archivo.writelines(contenido)

'''for i in range(1, len(contenido)):'''
modificar_dato('../../../../resource/doc/bares.txt', [1], 0, '')
