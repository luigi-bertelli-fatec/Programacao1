def valida_string(sTxt, minChar, maxChar):
    if(minChar <= len(sTxt) <= maxChar):
        return True
    else:
        return False
    

#MAIN
print(valida_string("Teste", 8, 10)) #Valor esperado: False
print(valida_string("Teste", 3, 8)) #Valor esperado: True