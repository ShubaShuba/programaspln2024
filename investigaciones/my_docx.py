#Braulio Yahir Gaitan Vargas
#Programa usando docx para sacar el texto de un archivo de word y lo guarda en un archivo de texto
#para la busqueda del archivo de word se usa filedialog el cual puede usarse para buscar cualquier archivo en la computadora
from docx import Document
import nltk
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import ttk




def word_to_text(input_file,output_file):
    doc = filedialog.askopenfilename()
    while doc[-5:] != ".docx":
        print("El archivo no es de tipo docx vuelva a intentarlo")
        doc = filedialog.askopenfilename()
    doc = Document(doc)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    with open(output_file, 'w') as file:
        for line in text:
            file.write(line + '\n')

# Reemplaza 'input.docx' y 'output.txt' con los nombres de tus archivos
word_to_text('prueba.docx', 'textoprueba.txt')

archivo = open("textoprueba.txt", "r")
texto = archivo.read()

#conteo del numero de palabras en el archivo de texto
palabras = texto.split()
print("Numero de palabras: ", len(palabras))

#conteo de numero de lineas del archivo de texto
lineas = texto.split("\n")
print("Numero de lineas: ", len(lineas))

#numero de palabras de un texto
palabra = input("Ingrese la palabra a buscar: ")
while palabra == "":
    print("Ingrese una palabra valida")
    palabra = input("Ingrese la palabra a buscar: ")
if palabra not in texto:
    print("La palabra no se encuentra en el texto")
else:
    print("Numero de veces que se repite la palabra: ", texto.count(palabra))

#palabras funcionales del texto
stopwords = nltk.corpus.stopwords.words('spanish')
palabras = texto.split()
palabras = [palabra for palabra in palabras if palabra.isalpha()]
palabras = [palabra for palabra in palabras if palabra.lower() not in stopwords]
print("Palabras funcionales: ", palabras)

#tokenizar el texto
tokens = nltk.word_tokenize(texto)
print("Tokenizacion del texto: ", tokens)

#eliminar palabras funcionales
tokens_limpios = [token for token in tokens if token.lower() not in stopwords]

print("Tokenizacion del texto sin palabras funcionales: ", tokens_limpios)
print("numero total de tokens: ", len(tokens))
print("numero total de tokens limpios: ", len(tokens_limpios))

#frecuencia
frecuencia = nltk.FreqDist(tokens_limpios)
print("Frecuencia de las palabras: ", frecuencia.most_common(10))

#grafica de la frecuencia
frecuencia.plot(10, cumulative=False)
plt.show()