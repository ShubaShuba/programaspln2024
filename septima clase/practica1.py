import nltk

def riqueza_lexica(tokens):
    tokens_conjunto = set(tokens)
    palabras_totales = len(tokens)
    palabras_unicas = len(tokens_conjunto)
    riqueza_lexica = palabras_unicas/palabras_totales
    return riqueza_lexica


carpeta = "C:\\Users\\pabli\\FIME\\"
archivo_nombre = "archivo_texto.txt"

with open(carpeta+archivo_nombre,"r") as archivo:
    texto=archivo.read()


tokens=nltk.word_tokenize(texto,"spanish")
riqueza_lexica=riqueza_lexica(tokens)
print(riqueza_lexica)

conteo_individual=tokens.count("de")
print(conteo_individual)
palabras_totales=len(tokens)
porcentaje=100*conteo_individual/palabras_totales
print(porcentaje," %")
