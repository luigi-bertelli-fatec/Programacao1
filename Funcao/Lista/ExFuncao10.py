def fibonnaci(iLim):
    if(iLim < 1):
        return []
    
    lista = [1, 1]
    idx = 1
    while(lista[idx - 1] + lista[idx] <= iLim):
        lista.append(lista[idx - 1] + lista[idx])
        idx += 1
    return lista

    
#MAIN
fib = fibonnaci(20)
for i in range(len(fib)):
    print(fib[i])