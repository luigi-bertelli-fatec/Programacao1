def valida_perfeito(iNum):
    soma = 0
    for i in range(1, (iNum // 2) + 1):
        if(iNum % i == 0):
            soma += i
    return soma == iNum


#MAIN
val = 6
if(valida_perfeito(val)):
    print(f"{val} é um número perfeito")
else:
    print(f"{val} não é um número perfeito")