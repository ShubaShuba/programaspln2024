import nltk

archivo_nombre = "archivo_texto.txt"
archivo = open(archivo_nombre, "r")

texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")

texto_nltk = nltk.Text(tokens)

distribucion = nltk.FreqDist(texto_nltk)

print(distribucion["zorro"])


info={"Nombre":"Braulio","Mi Apellido":"Gaitan"}
info["Edad"] = 21
info["Curso"] = "Ingenieria en computacion inteligente"
info["Universidad"] = "universidad de colima"
for dato in info:
    print(dato,":",info[dato])