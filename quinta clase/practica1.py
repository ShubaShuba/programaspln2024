import nltk


carpeta = "C:\\Users\\pabli\\FIME\\"
archivo_nombre = "archivo_texto.txt"

with open(carpeta+archivo_nombre,"r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

for token in tokens:
    print(token)

palabras_Total=len(tokens)
print("Total de palabras: ",palabras_Total)
