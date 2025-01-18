import random

def numero():
    return random.randint(1,10)


def sorteio(numero):
    while True:
        try:     
            usuario = int(input("faça sua jogada: "))
            if usuario < 1 or usuario > 10:
                print ("escolha um numero de 1 a 10")
                continue
            if usuario > numero and usuario <= 10:
                print ("opa opa, é mais abaixo")
            elif usuario < numero and usuario >=1:
                print ("ihh rapaiz, esta baixo demais ")
            elif usuario == numero:
                print ("mizeravi acertou")
                break
        except ValueError:
            print ("escolha uma opçao valida")


CONSTANTE_1 = numero()
CONSTANTE_2 = sorteio(CONSTANTE_1)

print(CONSTANTE_2)
