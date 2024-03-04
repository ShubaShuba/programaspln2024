carpeta = "C:\\Users\\pabli\\FIME\\"
archivo_nombre = "archivo_texto.txt"
#prueba de commit
with open(carpeta + archivo_nombre, "r") as archivo:
    contenido = archivo.read()

    palabras_lista = contenido.split()
    palabras_lista.sort()
    for palabra in palabras_lista:
        print(palabra)