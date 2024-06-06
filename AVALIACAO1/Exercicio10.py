n = int(input("Número de notas a serem digitadas: "))
soma = 0

for i in range(n):
    soma += float(input(f"Digite a {i + 1}ª nota: "))

print(f"Média: {(soma / n):.1f}")
