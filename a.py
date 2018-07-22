import speech_recognition as sr

r=sr.Recognizer()


audio='aa020.wav'

with sr.AudioFile(audio) as source:
    print('Say Something')
    audio=r.listen(source)
    print('Done')

try:
    text=r.recognize_google(audio)
    print(text)

except Exception as e:
    print(e)
