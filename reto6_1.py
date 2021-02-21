def calculadora(operacion):
    
    try:
        resultado = eval(operacion)
        print(f'{resultado}')
    except (SyntaxError, NameError, TypeError) as e:
        print('error')
        print(f'{e}')

    return resultado
if __name__ == "__main__":
    print('Calculadora')
    operacion = input("Ingresa la operacion que quieres realizar: ")
    calculadora(operacion)

