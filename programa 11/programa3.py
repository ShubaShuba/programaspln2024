'''Braulio Yahir Gaitan Vargas'''
import nltk
nltk.download('stopwords')
print("Braulio Yahir Gaitan Vargas")
carpeta_nombre="C://Users//pabli//FIME//6d//Optativa_oswaldo//OPTATIVA-PLN//"
archivo_nombre="archivo_texto.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
print("----------------------------------------------------------------------")
palabras_funcionales=nltk.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
    print(palabras_funcional)
print("----------------------------------------------------------------------")
tokens=nltk.word_tokenize(texto,"spanish")
tokens_limpios=[]
for token in tokens:
    if token not in palabras_funcionales:
        tokens_limpios.append(token)
print(tokens_limpios)
print(len(tokens))
print(len(tokens_limpios))
texto_limpio_nltk=nltk.Text(tokens_limpios)
distribucion_limpia=nltk.FreqDist(texto_limpio_nltk)
distribucion_limpia.plot(40)