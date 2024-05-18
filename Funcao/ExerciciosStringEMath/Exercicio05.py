palavra = input("Digite uma frase: ")
palavraContrario = palavra[-1: -len(palavra) - 1: -1]
if(palavra.lower() == palavraContrario.lower()):
    print("Essa frase é um palíndromo")
else:
    print("Essa frase não é um palíndromo")