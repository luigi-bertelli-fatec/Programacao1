def lista_perfeitos():
    lista = []
    i = 6
    while True:
        if(valida_perfeito(i)):
            lista.append(i)
        if(len(lista) == 5):
            break
        i += 1
    return lista
    
def valida_perfeito(iNum):
    soma = 0
    for i in range(1, (iNum // 2) + 1):
        if(iNum % i == 0):
            soma += i
    return soma == iNum


#MAIN
lstPerfeitos = lista_perfeitos()
print('=' * 20, " Lista Perfeitos ", '=' * 20)
for item in lstPerfeitos:
    print(item)