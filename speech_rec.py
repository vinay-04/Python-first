import speech_recognition

file="H:\\codes\\op.wav"
rec=speech_recognition.Recognizer()

with speech_recognition.AudioFile(file) as source:
    audio_data=rec.record(source)
    text=rec.recognize_google(audio_data)
file = open("eng.txt",'x')
file.write(text)
file.close()
print("done")