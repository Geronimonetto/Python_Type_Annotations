import speech_recognition as sr
import pyttsx3

rec = sr.Recognizer()
engine = pyttsx3.init()


with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    engine.say("Olá Seja bem vindo ao Robô Jarvis!! Diga seu nome")
    engine.runAndWait()
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    engine.say(f"Olá {texto}, O que deseja ?")
    engine.runAndWait()
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language = "pt-BR")
    palavra = texto
    if palavra =="entrar no sistema" or palavra=="Entrar no Sistema":
        engine.say("Deseja entrar no sistema ?")
        engine.runAndWait()
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language = "pt-BR")
        palavra = texto
        if texto =="sim desejo" or texto=="Sim desejo":
            engine.say("Aguarde, enquanto estamos carregando o sistema!!")
            engine.runAndWait()
