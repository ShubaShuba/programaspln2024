import nltk


carpeta = "C:\\Users\\pabli\\FIME\\"
archivo_nombre = "archivo_texto.txt"

with open(carpeta+archivo_nombre,"r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

tokens_conjunto = set(tokens)

palabras_totales = len(tokens)
palabras_unicas = len(tokens_conjunto)

riqueza_lexica = palabras_unicas/palabras_totales


print(riqueza_lexica)