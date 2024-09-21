class Menu:
    def menu():
        print("1 - Consultar informaciones")
        print("2 - Crear informacion")
        print("3 - Borrar informacion")
        print("4 - Nueva compra")
        print("0 - Salir")

    def menuConsultar():
        print("1 - Listar clientes")
        print("2 - Listar funcionarios")
        print("3 - Listar productos")
        print("4 - Listar compras")
        print("0 - Volver")

    def menuCrear():
        print("1 - Crear cliente")
        print("2 - Crear funcionario")
        print("3 - Crear producto")
        print("0 - Volver")

    def menuBorrar():
        print("1 - Borrar cliente")
        print("2 - Borrar funcionario")
        print("3 - Borrar producto")
        print("0 - Volver")

    def menuComprar():
        print("1 - Crear compra")
        print("2 - Suspender compra")
        print("0 - Volver")

    def mostrarArchivo(archivo):
        arch = open(archivo, 'rt')
        for linea in arch.readlines():
            print(linea)
        arch.close()

print('<< Menu is ok! >>')