original = input("Digite uma frase: ")
breakText = input("Digite uma palavra: ")

cont = original.upper().count(breakText.upper())
print(f"A palavra \"{breakText}\" aparece {cont} vezes nessa frase")
