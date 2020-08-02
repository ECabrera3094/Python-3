# Decoradores
def decorador(Resta):
    def mensaje(*args, **kwargs):
        print("Accion 1.")
        resultado = Resta(*args, **kwargs)
        return resultado
    return mensaje

@decorador
def Resta(num1, num2):
    return (num1 - num2)

if __name__ == '__main__':
    resultado = Resta(23, 9)
    print(resultado)