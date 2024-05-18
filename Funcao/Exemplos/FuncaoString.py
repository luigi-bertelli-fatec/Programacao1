#split(): Limpa o fim e o início de um string
print(("    SLA  ").strip())
sBruto = ",,,,,dsadsad,.bla"
print(sBruto.strip(",.bla"))
#replace(): Substitui texto dentro de uma string
sReplace = "garrafa 1 e garrafa 2"
sReplace = sReplace.replace("garrafa", "lata")
print(sReplace)
#split(): quebra uma string em uma  de strings separadas no caracter passado como param
sSplit = "python;c#;java;javascript;html"
lstSplit = sSplit.split(";")
print(lstSplit)
#count(): contabiliza as aparições de uma string dentro da outra
sCount = "Faculdade de tecnologia de americana"
sQuebra = " de "
print(sCount.count(sQuebra))
#Gerar lista de char
sTexto = "TESTE"
lst = list(sTexto)
print(lst)
#Separando string mãe em substrings
minha_string = "Exemplo de  na tela"
print(minha_string[3:]) # a partir do terceiro caracter
print(minha_string[-4:-1]) # os últimos 4 caracteres
#valida se existe texto em uma string
substr = minha_string[4:-2]
existe = "na" in minha_string
print(existe)
#pega a posição de uma string dentro de outra
pos = minha_string.find("na")
print(pos)
print(minha_string[pos: pos + 2])