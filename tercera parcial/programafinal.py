import pyttsx3
import speech_recognition as sr
from tkinter import filedialog
import tkinter as tk


def texto_a_audio(texto):
    # Inicializar el motor TTS (Text-to-Speech)
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
        
        # Guardar el audio en un archivo .wav
        with open("grabacion.wav", "wb") as f:
            f.write(audio.get_wav_data())

    try:
        texto = recognizer.recognize_google(audio, language="es-MX")
        print("Texto detectado:", texto)
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error en la solicitud al servicio de reconocimiento de voz; {0}".format(e))
    return None

def tranforma_wav_texto(audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio = recognizer.record(source)
    try:
        texto = recognizer.recognize_google(audio, language="es-MX")
        print("Texto detectado:", texto)
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(texto)
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error en la solicitud al servicio de reconocimiento de voz; {0}".format(e))
    return None


if __name__ == "__main__":

    def convertir_texto():
        texto = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if texto:
            texto_a_audio(texto)

    def convertir_audio():
        texto = audio_a_texto()
        if texto:
            print("Texto detectado:", texto)

    def reproducir():
        nombre_archivo = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
        if nombre_archivo:
            tranforma_wav_texto(nombre_archivo)

    root = tk.Tk()
    root.title("Programa Final")
    root.geometry("400x300")

    label = tk.Label(root, text="¿Qué deseas hacer?")
    label.pack()

    button1 = tk.Button(root, text="Texto a Audio", command=convertir_texto)
    button1.pack()

    button2 = tk.Button(root, text="Audio a Texto", command=convertir_audio)
    button2.pack()

    button3 = tk.Button(root, text="Reproducir audio", command=reproducir)
    button3.pack()

    button4 = tk.Button(root, text="Salir", command=root.quit)
    button4.pack()

    root.mainloop()
