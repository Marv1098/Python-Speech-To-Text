import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Talk")
    audio_text = r.listen(source)
    print("Times Up. Thanks")

    try:
        print("Text: " + r.recognize_google(audio_text))
    except:
        print("Sorry. I didn't get that")
