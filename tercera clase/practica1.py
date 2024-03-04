carpeta = ""
archivo = "archivo_texto.txt"

with open(archivo, "r") as file:
    lineas_listas=file.readlines()

total_lineas = len(lineas_listas)

num_linea = 1
lineas_vacias=0
lineas_texto=0

for lineas in lineas_listas:
    if lineas.strip() == ":":
        print("linea vacia")
        lineas_vacias=lineas_vacias+1
        continue
    
    print("Linea",num_linea,":",lineas)
    lineas_texto=lineas_texto+1
    num_linea=num_linea+1



print("Del total de lineas",total_lineas)

print("De las lineas vacias",lineas_vacias)

print("de las lineas con texto", lineas_texto)

#contar las lineas que contiene el archivo y lo indique
#cuando esa linea no contenga texto indique que esa linea esta vacia
#mostrar cuantas lineas tienen texto y cuantas no
