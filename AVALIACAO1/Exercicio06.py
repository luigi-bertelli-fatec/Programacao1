maior = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))

if(n2 > maior):
    maior = n2

if(n3 > maior):
    maior = n3

if(n4 > maior):
    maior = n4

print(f"O maior número digitado foi o {maior}")