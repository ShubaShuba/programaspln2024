import PyPDF2
import nltk
from tkinter import filedialog
from tkinter import ttk

def pdf_to_text(input_file,output_file):
    pdf = filedialog.askopenfilename()
    while pdf[-4:] != ".pdf":
        print("El archivo no es de tipo pdf vuelva a intentarlo")
        pdf = filedialog.askopenfilename()
    text = []
    with open(pdf, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_number in range(reader.numPages):
            page = reader.getPage(page_number)
            text.append(page.extract_text())
    with open(output_file, 'w') as file:
        for line in text:
            file.write(line + '\n')

# Reemplaza 'input.pdf' y 'output.txt' con los nombres de tus archivos
pdf_to_text('prueba.pdf', 'textoprueba.txt')


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
