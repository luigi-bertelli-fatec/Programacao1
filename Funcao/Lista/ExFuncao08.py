def valida_string(sTxt, lista):
    for i in range(len(lista)):
        if(lista[i] == sTxt):
            return True
    return False
    

#MAIN
print(valida_string("Teste", ["teste", "tst", "abc"])) #Valor esperado: False
print(valida_string("Teste", [3, "Teste", 8])) #Valor esperado: True