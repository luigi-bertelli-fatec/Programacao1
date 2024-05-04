def valida_perfeito(iNum):
    soma = 0
    for i in range(1, iNum):
        if(iNum % i == 0):
            soma += i
    return soma == iNum



#MAIN
if(valida_perfeito(6)):
    print("PERFEITO")
else:
    print("NÃO É PERFEITO")