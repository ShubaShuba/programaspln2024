c = 'C:\\Users\\pabli\\FIME\\'
e = 'archivo_texto.txt'
s = 'archivo_texto2.txt'

e2 = open(c + e , "r")

s2 = open(c + s ,"w")

t = e2.read()

t2 = t

s2.write(t2)


e2.close()
s2.close()

s3 = open(c + s, "r")
print(s3.read())
s3.close()

carpeta = 'C:\\Users\\pabli\\FIME\\'
archivo = 'archivo_texto.txt'
#palabra = "mira"
with open(c + e,"r" ) as archivo:
    texto = archivo.read()
    print(texto)

palabra = input("Escribe la palabra a buscar ")
if palabra in texto:
    print("se encontro la palabra")
else:
    print("no se encontro la palabra")
    




