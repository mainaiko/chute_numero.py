import random
from time import sleep

def aleatorio(min, max):
    return random.randint(int(min), int(max))

def compara (numero_usuario, numero_aleatorio):
    if numero_usuario > numero_aleatorio and numero_usuario <= 100:
        print ("opa opa, é mais abaixo")
    elif numero_usuario < numero_aleatorio and numero_usuario >=1:
        print ("ihh rapaiz, esta baixo demais ")
    elif numero_usuario == numero_aleatorio:
        print ("mizeravi acertou")


print("Bem vindo aos jogos")
sleep(1)
print("Qual o seu nome?")
nome = str(input(""))
print ("haha {nome} voce tem 10 chances de acertar o numero :)")
sleep(1)
print ("Deseja continuar?")
print ("1 para sim e 2 para nao")
opcao_1 = int(input(""))

