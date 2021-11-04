def es_primo(number):
    contador = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run():
    number = int(input('Escribe un numero: '))
    if es_primo(number):
        print('Es primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    run()