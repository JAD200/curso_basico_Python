import random

secure_number_generator = random.SystemRandom()

def generar_contrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    SIMBOLS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    SPACE = [' ']

    characters = MAYUS + MINUS + NUMS + SIMBOLS + SPACE
    contrasena = []

    for i in range(15):
        caracter_random = secure_number_generator.choice(characters)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    print('\n\t PASSWORD GENERATOR \n')
    print('generating password...')
    contrasena = generar_contrasena()
    print('This is your new password: ' + contrasena)


if __name__ == '__main__':
    run()
