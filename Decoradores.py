# Decorador
def decorador(mensaje):
    def complemento():
        print("Accion 1.")
        mensaje()
        print("Accion 2.")
    return complemento

@decorador
def mensaje():
    print("Hola Mundo.")

if __name__ == '__main__':
    m = mensaje()