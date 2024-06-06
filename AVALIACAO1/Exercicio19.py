def embaralha(sTxt):
    embaralhada = sTxt[-1: -len(sTxt) - 1: -1].lower()
    return embaralhada
    

sPalavra = input("Digite uma palavra: ")
print(f"{sPalavra} ao contrário é {embaralha(sPalavra)}")