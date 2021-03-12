import webbrowser
import urllib.request
import urllib.parse
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Talk")
    audio_text = r.listen(source)
    print("Times Up. Thanks")
    speech = r.recognize_google(audio_text)
    qstr = urllib.parse.quote(speech)
    print(qstr)
    thing = urllib.request.urlopen("https://advisors.vanguard.com/search-results?query=" + qstr)
    data = thing.read().decode('utf-8')
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    webbrowser.register('google-chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('google-chrome').open(data, new = 1, autoraise=True)
