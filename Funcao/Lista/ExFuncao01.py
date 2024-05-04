def maximo():
    fN1 = (float)(input("Digite 0 1º número: ")) 
    fN2 = (float)(input("Digite 0 2º número: "))
    if(fN1 > fN2):
        return fN1
    return fN2


#MAIN
print(f"O maior número digitado foi {maximo()}")