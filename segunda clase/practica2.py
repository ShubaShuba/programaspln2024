semana_laboral = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
print("Semana Laboral = ", semana_laboral)
print("Dia 1  =", semana_laboral[4])
semana_laboral[4]="Sabado"
print("Semana Laboral = ", semana_laboral)
semana_laboral[4]="Viernes"
longitud_lista = len(semana_laboral)
print("Longitud = ", longitud_lista)
posicion = semana_laboral.index("Miercoles")
print("posicion de Miercoles=", posicion)
semana_laboral.append("Sabado")
print("Semana Laboral = ", semana_laboral)
del semana_laboral[4]
print("Semana laboral", semana_laboral)
print("Dia 2  =", semana_laboral[1])
print("Dia 3  =", semana_laboral[2])
print("Dia 4  =", semana_laboral[3])
print("Dia 5  =", semana_laboral[4])