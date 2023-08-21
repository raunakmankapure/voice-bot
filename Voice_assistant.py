import pyttsx3
import wikipedia

voice = pyttsx3.init()
In = input("Searching wikipedia/google: ")
result = wikipedia.summary(In, sentences = 3)
print(result)
voice.say(result)
voice.runAndWait()

#before running the code in your machine , install pyttsx3 & wikipedia libraries from CLI with commands pip install pyttsx3 & pip install wikipedia respectivly 
