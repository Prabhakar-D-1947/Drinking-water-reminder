# import pyttsx3


# engine = pyttsx3.init()

# names = ["Prabhakar Dwivedi", "Nishant", "Aditya", "Abhay"]

# for name in names:
#     engine.say(f"Shout out to {name}")
#     engine.runAndWait()
#     engine.stop()




import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

names = ["Prabhakar Dwivedi", "Nishant", "Aditya", "Abhay"]

for name in names:
    speaker.Speak(f"Shout out to {name}")

