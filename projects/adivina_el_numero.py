import random


def run():
    contador = 0
    random_number = random.randint(1, 100)
    number_selected = int(input('Elige un número del 1 al 100: '))
    while number_selected != random_number:
        if number_selected < random_number:
            print('Busca un número mayor ')
            number_selected = int(input('Elige otro numero: '))
        else:
            print('Busca un número menor ')
            number_selected = int(input('Elige otro numero: '))
        contador += 1
    print('\n* * * * GANASTE! * * * *\n')
    print('Numero de intentos: ' + str(contador))


if __name__ == '__main__':
    run()