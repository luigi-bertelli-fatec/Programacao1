def divisores(num):
    cont = 0
    for i in range(1 , (num // 2) + 1):
        if (num % i == 0):
            cont += 1
    return cont
    

#MAIN
print(divisores(6)) #Valor esperado: 3
print(divisores(28)) #Valor esperado: 5