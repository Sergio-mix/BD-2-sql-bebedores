from _ast import alias

import file
import sql
import random
from datetime import datetime, timedelta


def main():
    if __name__ == '__main__':
        print()


main()

nombres = file.File().read(url="../../../../resource/doc/nombres.txt")
apellidos = file.File().read(url="../../../../resource/doc/apellidos.txt")

listaBebedores = []


def aliasRamdom(nombres, apellidos):
    random_Nombre = random.randint(0, 454)
    random_Apellido = random.randint(0, 102)
    return "bebedor " + nombres[random_Nombre] + " " + apellidos[random_Apellido]


def searchAlias(alias, lista):
    for i in lista:
        if i == alias:
            return True
    return False


def generateAlias(size):
    for i in range(0, size):
        alias = aliasRamdom(nombres, apellidos)
        if not searchAlias(alias, listaBebedores):
            listaBebedores.append(alias)


def generateGenero():
    aleatorio = random.randint(0, 1)
    if aleatorio == 0:
        return "M"
    else:
        return "F"


def get_rnd_date(start, end, fmt):
    s = datetime.strptime(start, fmt).date()
    e = datetime.strptime(end, fmt).date()

    delta = e - s

    return s + timedelta(days=(random.random() * delta.days))


try:
    generateAlias(1000)
    sql = sql.Sql()
    for i in listaBebedores:
        date = str(get_rnd_date("1960-01-01", "2005-01-01", "%Y-%m-%d"))
        alias = str(i)
        data = "null, " + alias + ", " + date + ", " + generateGenero() + ", 0"
        sql.set(
            table="bebedores",
            data=data)

    print(sql.get(table="bebedores"))
except Exception as e:
    print(e)
