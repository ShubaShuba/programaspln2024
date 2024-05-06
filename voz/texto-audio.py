import pyttsx3
import speech_recognition as sr
from tkinter import filedialog


def texto_a_audio(texto):
    # Inicializar el motor TTS (Text-to-Speech)
    #lee el texto y lo convierte en audio
    texto = open(texto, "r").read()
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(texto)
    engine.runAndWait()

def audio_a_texto():
    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Grabando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="es-MX")
        print("Texto detectado:", texto)
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error en la solicitud al servicio de reconocimiento de voz; {0}".format(e))

if __name__ == "__main__":
    opcion = input("¿Qué deseas hacer? (1) Texto a Audio, (2) Audio a Texto: ")

    if opcion == "1":
        print("Introduce el texto que deseas convertir a audio: ")
        texto = filedialog.askopenfilename()
        while texto == ".txt":
            print("Introduce un texto válido")
            texto = filedialog.askopenfilename()
        texto_a_audio(texto)
    elif opcion == "2":
        texto = audio_a_texto()
        if texto:
            print("Texto detectado:", texto)
    else:
        print("Opción no válida")
