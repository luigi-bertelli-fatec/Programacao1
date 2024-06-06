def contaConsoantes(sTxt):
    consoantesCont = dict()
    for i in range(len(sTxt)):
        char = sTxt[i].lower()
        if(char in ('a', 'e', 'i', 'o', 'u')):
            if(char in consoantesCont):
                consoantesCont[char] += 1
            else:
                consoantesCont[char] = 1
    return consoantesCont


sTxt = input("Digite um texto: ")
dictTxt = contaConsoantes(sTxt)
print("Vogais digitadas:")
for i in dictTxt:
    if(dictTxt[i] == 1):
        print(f"{dictTxt[i]} letra '{i}'")
    else:
        print(f"{dictTxt[i]} letras '{i}'")