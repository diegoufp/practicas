def food_saucer(order):

    if order == 1:
        return 60
    elif order == 2:
        return 80
    elif order == 3:
        return 30
    elif order == 4:
        return 20
    elif order == 5:
        return 30
    elif order == 7:
        return 40
    elif order == 8:
        return 20
    else:
        print('No esta dentro de las opciones')
        return 0

def tip(saurcer):

    yes_or_not = int(input("""
    Quieres dejar propina? (Elige el numero de la opcion)
                            
                        [1] Yes
                        [2] No
    """))

    if (yes_or_not == 2) or (yes_or_not == 'No') or (yes_or_not == 'no'):
        return 0
    elif (yes_or_not == 1) or (yes_or_not == 'Yes') or (yes_or_not == 'yes'):
        percentage = int(input('Que porcejate quiere dejar de propina?: '))
        percentag = percentage / 100
        perc = saurcer * percentag

        return perc

if __name__ == "__main__":

    print('welcome to the restaurant of another world\n')
    print('Que desea ordenar?: ')
    order = int(input("""
    (Elige el numero de la opcion)
    Menú:
            [1] Especial del dia: 
                   - Chuleta empanizada.
                   - Agua de limon.
                   - Un flan.
            
            [2] Langostinos fritos:
                    - Camarones empanizados
                    - Pan
                    - Salsa tartara
                    - Un plato de sopa
                    
            [3] Espagueti con salsa boloñesa
            
            [4] Café
            
            [5] Parfait de chocolate
            
            [6] Omurice

            [7] Filete de tofu

            [8] Arroz 
    """ ))

    saurcer = food_saucer(order)
    percentage = tip(saurcer)
    account = saurcer + percentage
    print(f'Cuenta:\nTotal consumido: {saurcer}\nPorcentaje de propina: {percentage}\nTotal a pagar: {account}')
    
