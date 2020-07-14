def operacion(valor_1, operador, valor_2):

    if operador == '+':
        return valor_1 + valor_2
    elif operador == '/':
        return valor_1 / valor_2
    elif operador == '-':
        return valor_1 - valor_2
    elif operador == '*':
        return valor_1 * valor_2
    elif operador == '**':
        return valor_1 ** valor_2
    else:
        return 'error'

if __name__ == "__main__":
    input_1 = float(input('Ingresa un numero: '))
    operador = input('Ingresa el operador: ')
    input_2 = float(input('Ingresa el segundo numero: '))

    resultado = operacion(input_1, operador, input_2)
    print(resultado)