def primo(limite):

    for n in range(2, limite + 1):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
        # loop fell through without finding a factor
            print(n, 'is a prime number')

if __name__ == '__main__':
    limite = int(input('Ingresa un limite para se sencuencia de numeros: '))

    primo(limite)