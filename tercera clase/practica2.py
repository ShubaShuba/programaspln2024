import os

carpeta = "C:\\Users\\pabli\\FIME\\"

archivos_lista = os.listdir(carpeta)

for archivo_nombre in archivos_lista:
    print(archivo_nombre)