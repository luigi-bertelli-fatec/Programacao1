import math

valorVenda = float(input("Valor da venda: "))
desconto = float(input("Percentual de desconto: ")) / 100

valorFinal =  math.floor(valorVenda - (valorVenda * desconto))
print(f"Valor final: {valorFinal}")