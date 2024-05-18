import math
import random

#Arredondamentos
fNum = 4.6
#Arredonda numero para casa superior mais próxima
print(math.ceil(fNum))
#Arredonda numero para casa inferior mais próxima
print(math.floor(fNum))
#Arredonda numero para cas mais próxima
print(round(fNum))

#Fatorial
print(math.factorial(6))

#Pi
print(math.pi)

#random
#random padrão gera número de 0.0-1.0
print(random.random())
#randint(ini, fim) - gera valores inteiro de ini até fim
print(random.randint(4, 9))
#randint(ini, fim) - gera valores flutuantes de ini até fim
print(random.uniform(4, 9))