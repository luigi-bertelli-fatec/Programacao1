num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite um número real: "))

conta1 = num1 * num2
conta2 = (num1 * 3) + num3
conta3 = num3 ** 3

print(f"({num1} x 2) x ({num2} / 2) = {conta1}")
print(f"({num1} x 3) + {num3} = {conta2}")
print(f"{num3}³ = {conta3}")