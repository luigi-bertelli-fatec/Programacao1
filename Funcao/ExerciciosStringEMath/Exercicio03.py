import random

rand = random.randint(1, 9)
num = (int)(input("Digite um número de 1 a 9: "))
while rand != num:
    num = (int)(input("Número incorreto!!! Digite um número de 1 a 9: "))
print("PARABÉNS!!!! Você acertou.")