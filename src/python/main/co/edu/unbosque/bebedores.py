import random
from datetime import datetime, timedelta
import sql


class Bebedores:
    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos

    def aliasRamdom(self, nombres, apellidos, i):
        random_Nombre = random.randint(0, 454)
        random_Apellido = random.randint(0, 102)
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

    def generateBebedores(self, size, table):
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
