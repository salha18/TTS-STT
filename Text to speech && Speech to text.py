from os import close
import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import speech_recognition as sr
api =IAMAuthenticator("7JoWwmButvQibXGKAAbs7C6vbhwjVseWv2bkRpBbek59")
text_2_speech=TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/d0884b35-e7d9-4a43-af02-27780b92feb8")

r=sr.Recognizer()
with sr.Microphone()as source:
    print("Speak Anything: ")
    sound=r.listen(source)
try:
    text=r.recognize_google(sound)
    print("You said: {}" .format(text))
except:
    print("Sorry could not recognize your voice")

myfile=open('STT.txt','w')
myfile.write(format(text))
myfile.close()

with open("STT.txt") as text_file:
        data=text_file.read()
        text_file.close()
   
with open("TTS.mp3","wb") as audio:
    audio.write(text_2_speech.synthesize(data,accept="audio/mp3").get_result().content)

