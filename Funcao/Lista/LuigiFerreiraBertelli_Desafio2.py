def conversao_binario():
    while True:
        if(input("Deseja continuar com a conversão de um byte para decimal ([N] - Sair / Outro - Continuar)? ").strip().upper() == 'N'):
            return
        sBinario = input("Digite um byte : ").strip()
        while(not valida_binario(sBinario)):
            sBinario = input("Número passado não está na base binária ou não possui 8 dígitos, por favor digite novamente: ").strip()
        iDecimal = calcula_binario(sBinario)
        print(f"Resultado: {sBinario}₂ = {iDecimal}₁₀\n")
    
def valida_binario(sBin):
    tam = len(sBin)
    if(tam != 8):
        return False
    
    for i in range(tam):
        if('0' != sBin[i] != '1'):
            return False
    return True

def calcula_binario(sBin):
    soma = 0
    tam = len(sBin)
    orderedBin = sBin[-1:-(tam + 1):-1]
    listaBin = list(orderedBin)
    for i in range(len(listaBin)):
        if(listaBin[i] == '1'):
            soma += (2 ** i)
    return soma


#MAIN
conversao_binario()