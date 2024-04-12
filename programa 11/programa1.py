# -*- coding: utf-8 -*-

'''
El ejercicio consiste en encontrar todas las "palabras" de 3 o 4 letras
- Se entiende por "palabra" CUALQUIER coosa entre espacios
'''

import re
import nltk

carpeta_nombre="C://Users//pabli//FIME//6d//Optativa_oswaldo//OPTATIVA-PLN//"
archivo_nombre="archivo_texto.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

expresion_regular=re.compile(r"...? ")

resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))