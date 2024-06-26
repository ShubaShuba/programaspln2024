#Braulio Yahir Gaitan Vargas
#Programa usando nltk para sacar el texto de una pagina web y lo guarda en un archivo de texto

import nltk
import urllib.request

input("Quiere usar una Web Personalizada?")
if input == "si" or input == "Si":
    url = input("Ingrese la url de la pagina web: ")
else:      #la URL colocada puede que futuramente ya no exista por caducidad
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

buscar_palabra = input("Ingrese la palabra que desea buscar en la pagina web: ")
num_palabras = texto_nltk.count(buscar_palabra)
print("Numero de veces que aparece la palabra: ", num_palabras)

num_palabras = len(texto_nltk)
print("Numero de palabras: ", num_palabras)

#esta funcion exacta no funciona correctamente debido a que la funcion que extrae los datos los obtiene de manera cruda sin seguir ningun formato
num_lineas = texto_nltk.count("\n")
print("Numero de lineas: ", num_lineas)



#Parte 2 del trabajo

#Cargar palabras funcionales en español
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
    print(palabras_funcional)

#tokenizar limpiamente
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

#impresiones

print(tokens_limpios)
print("Numero de palabras: ", len(tokens))
print("Numero de palabras limpias: ", len(tokens_limpios))

#crear un objeto Text de NLTK y calcular la distribucion de frecuencia
texto_nltk = nltk.Text(tokens_limpios)
frecuencia = nltk.FreqDist(texto_nltk)

#Graficar las 40 palabras mas comunes
frecuencia.plot(40)



