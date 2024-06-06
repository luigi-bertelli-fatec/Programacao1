def ImprimePiramide(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i , end=(" " if (j < i -1) else "\n"))
        
        
ImprimePiramide(int(input("Digite um número inteiro: ")))