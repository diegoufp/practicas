def primos(limit):

    for x in range(2,limit + 1):
        if x == 2:
            print(x)
        elif x == 3:
            print(x)
        elif x == 5:
            print(x)
        elif x == 7:
            print(x)
        else:
            if x%2 != 0 and x%3 != 0 and x%5 != 0 and x%7 != 0 and x%x == 0:
                print(x)
            else:
                continue

if __name__ == "__main__":
    limit = int(input('Ingresa un numero limite para calcular los numero primos: '))

    primos(limit)