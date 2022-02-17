import file
import sql


def main():
    if __name__ == '__main__':
        print()


main()

nombres = file.File().read(url="../../../../resource/doc/nombres.txt")
apellidos = file.File().read(url="../../../../resource/doc/apellidos.txt")

sql = sql.Sql()
sql.set(table="bebedores", data="1, 'a', '2022-02-16', 'M', 1")
print(sql.get(table="bebedores"))
