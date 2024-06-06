listaIdades = []
listaAlturas = []

for i in range(30):
    print(f"Digite a idade e altura do {i+1}º aluno")
    listaIdades.append(int(input("Idade: ")))
    listaAlturas.append(float(input("Altura: ")))
    print("\n")

mediaAltura = 0
for j in range(len(listaAlturas)):
    mediaAltura += listaAlturas[j] / len(listaAlturas)

cont = 0
for k in range(len(listaIdades)):
    if(listaIdades[k] >= 13 and listaAlturas[k] < mediaAltura):
        cont += 1

if(cont > 1):
    print(f"{cont} alunos com mais de 13 anos estão abaixo da média de altura da lista")
elif(cont > 0):
    print(f"{cont} aluno com mais de 13 anos está abaixo da média de altura da lista")
else:
    print(f"nenhum aluno com mais de 13 anos está abaixo da média de altura da lista")