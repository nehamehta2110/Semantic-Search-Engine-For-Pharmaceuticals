import speech_recognition as sr
#import webbrowser as wb
#import speak

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source,timeout=1,phrase_time_limit=10)
    print ('Done!')
try:
    text = r.recognize_google(audio)
    print('Google thinks you said:\n' + text)
except Exception as e:
    print (e)