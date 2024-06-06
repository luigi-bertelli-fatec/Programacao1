val = int(input("Digite um número maior que 0 e menor que 1000: "))
while not( 0 < val < 1000):
    val = int(input("Valor deve ser maior que 0 e menor que 1000, tente novamente: "))

centenas = val // 100
centenasStr = ""
if(centenas > 0):
    centenasStr += f"{centenas} centena"
    if(centenas > 1):
        centenasStr += "s"

dezenas = (val % 100) // 10
dezenasStr = ""
if(dezenas > 0):
    dezenasStr += f"{dezenas} dezena"
    if(dezenas > 1):
        dezenasStr += "s"

unidades = (val % 100) % 10
unidadesStr = ""
if(unidades > 0):
    unidadesStr += f"{unidades} unidade"
    if(unidades > 1):
        unidadesStr += "s"

sTexto = f"{val} = "
if(len(centenasStr) > 0):
    sTexto += centenasStr
    if(len(dezenasStr) > 0 and len(unidadesStr) > 0):
        sTexto += f", "
    elif(len(dezenasStr) > 0 or len(unidadesStr) > 0):
        sTexto += f" e "

if(len(dezenasStr) > 0):
    sTexto += dezenasStr
    if(len(unidadesStr) > 0):
        sTexto += " e "

if(len(unidadesStr) > 0):
    sTexto += unidadesStr

print(sTexto)