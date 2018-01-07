import speech_recognition as sr
import parseSpeech as ps
import textMath as tm


r = sr.Recognizer()
r.pause_threshold = 1

while(1):
    
    with sr.Microphone() as audioSource:
        print("Say a math problem...")
        audioData = r.listen(audioSource)
    try:
        speechText=r.recognize_google(audioData)
    except sr.UnknownValueError:
        print("Try agian")
        continue
    print(speechText)
    speechText=ps.parseSpeech(speechText)
    print(speechText)
    speechText=speechText.split()

    result = tm.textMath(speechText)

    if result==None:
        print("Try agian")
    else:    
        print("= " + str(result))

    



    



    
