import random

def start():
    (ponto, continuar) = primeiraJogada()
    
    while continuar:
        if(input("Posso rolar os dados (S - Continuar / N - Parar)? ").upper() == "N"):
            break
        jogada = rolaDados()
        if(validaJogada(ponto, jogada)):
            break
    print("\nFIM DE JOGO")
            
        
def validaJogada(ponto, jogada):
    print(f"JOGADA: {jogada} - PONTO: {ponto}")
    if(jogada == 7):
        print("Você perdeu! Infelizmente você tirou 7 nos dados e perdeu, tente novamente.")
        return True
    elif(jogada == ponto):
        print("Parabéns você venceu!")
        return True
    else:
        print("Quase lá, bora pra próxima.\n")
        return False
        
def primeiraJogada():
    ponto = rolaDados()
    continuar = True
    print(f"PRIMEIRA JOGADA: {ponto}\n")
    if(ponto == 7 or ponto == 11):
        print(f"Você tirou um {ponto} isso significa que você é um natural e ganhou o jogo, parabéns!!!")
        continuar = False
    elif(ponto == 2 or ponto == 3 or ponto == 12):
        print(f"CRAPS!!! Ah não você tirou {ponto} nos dados e perdeu, tente novamente.")
        continuar = False
    return (ponto, continuar)
    
def rolaDados():
    min = 2
    max = 12
    return random.randint(min, max)


start()