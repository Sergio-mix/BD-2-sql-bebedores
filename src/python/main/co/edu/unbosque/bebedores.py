import random
from datetime import datetime, timedelta
import sql


class Bebedores:
    def __init__(self, nombres, apellidos, cervezas, bares):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cervezas = cervezas
        self.bares = bares

    def aliasRamdom(self, nombres, apellidos, i):
        random_Nombre = random.randint(0, len(nombres) - 1)
        random_Apellido = random.randint(0, len(apellidos) - 1)
        return "bebedor " + nombres[random_Nombre] + " " + apellidos[random_Apellido] + "_" + str(i) + "__"

    def generateGenero(self):
        if random.randint(0, 1) == 0:
            return "M"
        else:
            return "F"

    def get_rnd_date(self, start, end, fmt):
        s = datetime.strptime(start, fmt).date()
        e = datetime.strptime(end, fmt).date()
        delta = e - s
        return s + timedelta(days=(random.random() * delta.days))

    def generate_Bebedores(self, size, table):
        try:
            data = sql.Sql()
            print("Generando bebedores...")
            aux = 1
            for i in range(0, size):
                date = "'" + str(self.get_rnd_date("1960-01-01", "2005-01-01", "%Y-%m-%d")) + "'"
                data.add(table=table,
                         data="null, " + "'" + self.aliasRamdom(self.nombres, self.apellidos,
                                                                i) + "'" + ", " + date + ", " + "'" + self.generateGenero() + "'" + "," + str(
                             aux))
                aux += 1
                print("Bebedores generados")
        except Exception as e:
            print(e)
            print("Error al generar bebedores")

    def generate_Cervezas(self, size, table):
        try:
            data = sql.Sql()
            print("Generando servezas...")
            for i in range(0, size):
                data.add(table=table,
                         data="null, " + "'" + self.cervezas[random.randint(0, len(self.cervezas) - 1)] + "_" +
                              self.cervezas[
                                  random.randint(0, len(self.cervezas) - 1)] + "', " + str(
                             random.randint(0, 5)))

        except Exception as e:
            print(e)
            print("Error al generate Servezas")

    def generate_Gustar(self, size, table, bebedores, cervezas):
        try:
            data = sql.Sql()
            print("Generando Tabla de gusta")
            for i in range(0, size):
                data.add(table=table,
                         data="null, " + ", '" + bebedores["id"][random.randint(0, len(bebedores) - 1)] + "', " +
                              cervezas["id"][random.randint(0, len(cervezas) - 1)] + "_")
        except Exception as e:
            print(e)
            print("Error al generate Gustar")

    def generate_Bares(self, size, table):
        try:
            data = sql.Sql()
            print("Generando Bares...")
            for i in range(0, size):

                data.add(table=table,
                         data="null, " + "'" + self.aliasRamdom(self.nombres, self.apellidos,
                                                                i) + "'" + ", " + "'" + self.generateGenero() + "'" + "," + str(
                             random.randint(0, 5)))
                print("Bares generados")
        except Exception as e:
            print(e)

