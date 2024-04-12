import nltk
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Descargar los recursos necesarios para NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def recognize_entities(text):
    # Tokenizar el texto en palabras
    words = word_tokenize(text)
    # Etiquetar las palabras con partes del discurso (POS tagging)
    tagged_words = pos_tag(words)
    # Aplicar el reconocimiento de entidades nombradas (NER)
    named_entities = ne_chunk(tagged_words)
    return named_entities

# Ejemplo de texto
texto = "Barack Obama was born in Hawaii and he served as the President of the United States."

# Reconocer entidades nombradas en el texto de ejemplo
entidades_nombradas = recognize_entities(texto)

# Imprimir las entidades nombradas encontradas
print(entidades_nombradas)
