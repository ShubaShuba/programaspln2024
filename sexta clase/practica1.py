import nltk



carpeta = "C:\\Users\\pabli\\FIME\\"
archivo_nombre = "archivo_texto.txt"

with open(carpeta+archivo_nombre,"r") as archivo:
    texto=archivo.read()    


tokens = nltk.word_tokenize(texto, "spanish")

texto_nltk = nltk.Text(tokens)

print(texto_nltk.similar("esto"))

print(texto_nltk.concordance("rapido"))

