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


def aliasRamdom(nombres, apellidos, i):
    random_Nombre = random.randint(0, 454)
    random_Apellido = random.randint(0, 102)
    return "bebedor " + nombres[random_Nombre] + " " + apellidos[random_Apellido] + "_" + str(i) + "__"


def generateAlias(size):
    for i in range(0, size):
        listaBebedores.append(aliasRamdom(nombres, apellidos, i))


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
    generateAlias(10_000)
    sql = sql.Sql()
    for i in listaBebedores:
        date = "'" + str(get_rnd_date("1960-01-01", "2005-01-01", "%Y-%m-%d")) + "'"
        sql.add(
            table="bebedores",
            data="null, " + "'" + i + "'" + ", " + date + ", " + "'" + generateGenero() + "'" + ", 0")
except Exception as e:
    print(e)
