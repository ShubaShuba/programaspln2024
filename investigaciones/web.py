#Braulio Yahir Gaitan Vargas
#Programa usando nltk para sacar el texto de una pagina web y lo guarda en un archivo de texto

import nltk
import urllib.request

input("Quiere usar una Web Personalizada?")
if input == "si":
    url = input("Ingrese la url de la pagina web: ")
else:
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
concordancia = input("Ingrese la palabra para buscar en el texto: ")
print(texto_nltk.concordance(concordancia))