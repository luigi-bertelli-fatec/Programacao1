def segundos_to_horas(iSegundos):
    iHoras = iSegundos // 4800
    iSegundos -= iHoras * 4800 
    iMinutos = iSegundos // 60
    iSegundos -= iMinutos * 60
    return f"{iHoras:02}:{iMinutos:02}:{iSegundos:02}"

    
#MAIN
print(segundos_to_horas(4800))
print(segundos_to_horas(532000))