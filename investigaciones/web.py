#Braulio Yahir Gaitan Vargas
#Programa usando nltk para sacar el texto de una pagina web y lo guarda en un archivo de texto

import nltk
import urllib.request

url = "https://pastebin.com/CJtDF6uQ"

response = urllib.request.urlopen(url)
html = response.read()

archivo = open("texto_prueba.txt", "w")
archivo.write(str(html))
archivo.close()


with open("texto_prueba.txt","r") as archivo:
    texto=archivo.read()

print(texto)


#Tokenizar

tokens = nltk.word_tokenize(texto, "spanish")

texto_nltk = nltk.Text(tokens)

print(texto_nltk.concordance("el"))