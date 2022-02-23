import file
import bebedores


def main():
    if __name__ == '__main__':
        print()


main()

nombres = file.read(url="../../../../resource/doc/nombres.txt")
apellidos = file.read(url="../../../../resource/doc/apellidos.txt")
servezas = file.read(url="../../../../resource/doc/servezas.txt")

bebedores_ = bebedores.Bebedores(nombres, apellidos, servezas)
bebedores_.generar_bebedores(size=1_000, table="bebedores")
