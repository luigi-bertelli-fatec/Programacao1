tam = 4
media = 0
for i in range(tam):
    media += float(input(f"Digite a {i + 1}ª nota: ")) / tam

print(f"Média: {media:.1f}")