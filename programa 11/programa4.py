# -*- coding: utf-8 -*-

'''
El ejercicio consiste en encontrar todos los documentos DOC y DOCX de una carpeta usando
expresiones regulares.
'''

import os
import re

carpeta_nombre="C://Users//pabli//OneDrive//Desktop//Tareas"

archivos_lista=os.listdir(carpeta_nombre)

expresion_regular=re.compile(r"\.docx?$")

for archivo_nombre in archivos_lista:
    resultado_busqueda=expresion_regular.search(archivo_nombre)
if resultado_busqueda:
    print(resultado_busqueda.group(0))
print(archivo_nombre)