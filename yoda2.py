import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

ouvido = sr.Recognizer()
yoda = pyttsx3.init()

def executar_comando():
    try:
        with sr.Microphone() as mic:
            print("Estou ouvindo...")
            voz = ouvido.listen(mic)
            comando = ouvido.recognize_google(voz, language="pt-BR")
            comando = comando.lower()  # Converte o comando para minúsculas
            return comando
           
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o que você disse.")
        return ""
    except sr.RequestError:
        print("Erro ao se conectar com o serviço de reconhecimento de voz.")
        return ""
   

def realizar_acao(comando):
        if 'ioda' in comando:
            comando = comando.replace('ioda', '')
        elif 'yoda' in comando:
            comando = comando.replace('ioda', '')


        if 'horas' in comando:
            hora = datetime.datetime.now().strftime('%H:%M')
            yoda.say(f'Agora são {hora}')
            yoda.runAndWait()

        elif 'procure por' in comando:
            procura = comando.replace('pesquise', '')
            wikipedia.set_lang('pt')
            procura = comando.replace('procure por', '')
            resposta = wikipedia.summary(procura, 2)
            yoda.say(resposta)
            yoda.runAndWait()

        elif 'reproduza' in comando:
            conteudo = comando.replace('reproduza', '')
            resposta = pywhatkit.playonyt(conteudo)
            yoda.say(f'Reproduzindo {conteudo} no youtube')
            yoda.runAndWait()

realizar_acao()


while True:
    comando = executar_comando()
    if comando:
        realizar_acao(comando)
    