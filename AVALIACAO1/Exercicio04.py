import math

area = float(input("Digite a área a ser pintada em m²: "))
latas = math.ceil((area / 3) / 18)
valorTotal = latas * 280.0

print(f"Para essa pintura serão necessárias {latas} lata(s) de tinta.")
print(f"Preço total: R${valorTotal:.2f}")