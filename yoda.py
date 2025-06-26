import pyttsx3
import speech_recognition as sr

ouvido = sr.Recognizer()
voz=pyttsx3.init()

def falar(texto):
    print(f'Assistente: {texto}')
    voz.say(texto)
    voz.runAndWait()

def ouvir():
    with sr.Microphone() as mic:
        print('Ouvindo...')
        audio= ouvido.listen(mic)
    try:
        comando=ouvido.recognizer_google(audio, language='pt-BR')
        print(f'Você disse: {comando}')
        return comando.lower()
    except sr.UnknownValueError:
        falar('Desculpe não entendi')
        return ""
    except sr.RequestError:
        falar('Não consegui abrir o sistema audio')
        return ""

falar('Ola boa, tarde!')

# a voz que vais ser usada para responder, dá para colocar voz personalizada, nesse programa está a voz padrão do pyttsx3