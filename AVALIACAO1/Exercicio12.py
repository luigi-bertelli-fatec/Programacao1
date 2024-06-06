listaChar = []
for i in range(10):
    listaChar.append(input(f"Digite o {i+1}º caracter: "))

listaConsoantes = []
for j in range(len(listaChar)):
    if(listaChar[j].upper() not in ('A' , 'E', 'I', 'O', 'U')):
        listaConsoantes.append(listaChar[j].upper())

if(len(listaConsoantes) > 1):
    print(f"{len(listaConsoantes)} consoantes foram lidas")
elif(len(listaConsoantes) > 0):
    print(f"{len(listaConsoantes)} consoante foi lida")
else:
    print(f"nenhuma consoante foi lida")

for k in range(len(listaConsoantes)):
    print(listaConsoantes[k])