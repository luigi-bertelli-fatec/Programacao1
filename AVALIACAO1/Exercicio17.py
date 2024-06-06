def Digitos(num):
    contDigitos = len(str(num))
    if(contDigitos > 1):
        print(f"{num} tem {contDigitos} dígitos")
    else:
        print(f"{num} tem apenas um dígito")
    


Digitos(int(input("Digite um número inteiro: ")))