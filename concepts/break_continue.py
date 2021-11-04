from typing import Text


def run():
# CONTINUE
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

# BREAK en numeros
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

# BREAK en letras
    text = input('Escribe un texto: ')
    for letra in text:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()