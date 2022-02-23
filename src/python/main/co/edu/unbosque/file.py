def read(url):
    lista = []
    with open(url, "r") as archivo:
        for linea in archivo:
            lista.append(linea.strip())
    return lista


class File:
    pass
