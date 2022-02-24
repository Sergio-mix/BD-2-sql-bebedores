import file
import bebedores
import sql

def main():
    if __name__ == '__main__':
        print()


main()

nombres = file.read(url="../../../../resource/doc/nombres.txt")
apellidos = file.read(url="../../../../resource/doc/apellidos.txt")
cervezas = file.read(url="../../../../resource/doc/cervezas.txt")
bares = file.read(url="../../../../resource/doc/bares.txt")

data = sql.Sql()
bebedores_ = bebedores.Bebedores(nombres, apellidos, cervezas, bares)
bebedores_.generate_Bebedores(size=1_000, table="bebedores")
bebedores_.generate_Cervezas(size=1_000, table="cervezas")
bebedores_.generate_Gustar(size=1_000, table="gustar",bebedores=data.get("bebedores"), cervezas=data.get("cervezas"))
