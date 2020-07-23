def calculadora(operation):

    try:
        result = eval(operation)
    except (NameError, TypeError, SyntaxError) as e:
        print(f'{e}\n')
        print(f'No introdujiste un valor numérico, de operación o la la operacion esta mal escrita. Intenta de nuevo.')
        return 0
    else:
        if type(result) == int or type(result) == float or type(result) == complex:
            return result
        else:
            return 0

if __name__ == '__main__':
    operation = input('Ingresa la operacion que quieres resolver: ')

    result = calculadora(operation)

    print(result)

