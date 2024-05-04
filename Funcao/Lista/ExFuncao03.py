def multiplo(n1, n2):
    if(n1 % n2==0):
        return True
    else:
        return False
    

#MAIN
print(multiplo(8,4)) #Valor esperado: True
print(multiplo(7,3)) #Valor esperado: False
print(multiplo(5,5)) #Valor esperado: True