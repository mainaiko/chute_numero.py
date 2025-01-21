import random
from time import sleep

def aleatorio(min, max):
    return random.randint(int(min), int(max))

def compara (numero_usuario, numero_aleatorio):
    if numero_usuario > numero_aleatorio and numero_usuario <= 100:
        print ("opa opa, é mais abaixo")
        sleep(1)
        return False
    elif numero_usuario < numero_aleatorio and numero_usuario >=1:
        print ("ihh rapaiz, esta baixo demais ")
        sleep(1)
        return False
    elif numero_usuario == numero_aleatorio:
        print ("mizeravi acertou")
        sleep(1)
        return True


print("Bem vindo aos jogos")
sleep(1)
print("Qual o seu nome?")
nome = str(input(""))
print (f"haha {nome} voce tem 10 chances de acertar o numero :)")
sleep(1)
print ("o numero se encontra entre 1 e 100")
sleep(2)
print ("Deseja continuar?")
print ("1 para sim e 2 para nao")
opcao_1 = int(input(""))

if opcao_1 == 1:

    pontuacao_usuario = 10

    sorteio = aleatorio(1, 100)
    
    comparado = False

    while not comparado and pontuacao_usuario > 0:
        
        try:
            valor_usuario = int(input("faça seu lance: "))
        except ValueError:
            print ("valor informado nao se trata de um numero, digite um numero de 1 a 100")
            continue

        comparado = compara(valor_usuario, sorteio)

        if not comparado:
            print ("tente novamente")
            pontuacao_usuario -= 1
            if comparado == False and pontuacao_usuario == 0:
                print (f"rapaz vc perdeu memo em {nome}, o numero era", sorteio)
                break
        
        else:
            print ("parabenssss")

else:
    print ("ta bao tchau")

    



