def LerDados():
    sNome = input("Digite seu nome: ")
    cGenero = LerGenero()
    fAltura = (float)(input("Digite sua altura: "))
    ExibeDados(sNome, Calcula(cGenero, fAltura))

def LerGenero():
    sTexto = "Digite seu gênero (M/F): "
    while True:
        sGen = input(sTexto).upper()
        if(sGen in ('M', 'F')):
            break
        sTexto = "Gênero INCORRETO!!! Digite seu gênero (M/F): "
    return sGen

def Calcula(genero, altura):
    if(genero == 'M'):
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7

def ExibeDados(nome, pesoIdeal):
    print(f"{nome}, seu peso ideal será {pesoIdeal:.1f}kg")

#MAIN
LerDados()