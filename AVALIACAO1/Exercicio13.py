listaNum = []
for i in range(10):
    listaNum.append(int(input(f"Digite o {i+1}º número: ")))
    
somaQuadrados = 0
for j in range(len(listaNum)):
    somaQuadrados += listaNum[j] ** 2

print(f"A soma dos quadrados dos números digitados é {somaQuadrados}")