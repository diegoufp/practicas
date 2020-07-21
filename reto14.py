def primos(limit):

    if limit%2 != 0 and limit%3 != 0 and limit%limit == 0:
        print(f'{limit} Este es un numero primo')
    else:
        print(f'{limit} Este no es un numero primo')

if __name__ == "__main__":
    limit = int(input('Ingresa un numero limite para calcular los numero primos: '))

    primos(limit)