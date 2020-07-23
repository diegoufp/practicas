def calculadora(operation):

    try:
        result = eval(operation)
        return result
    except (NameError, TypeError, SyntaxError) as e:
        print(f'{e}\n')
        print(f'No introdujiste un valor numérico, de operación o la la operacion esta mal escrita. Intenta de nuevo.')
    else:
        return result

if __name__ == '__main__':
    operation = input('Ingresa la operacion que quieres resolver: ')

    result = calculadora(operation)

    print(result)

