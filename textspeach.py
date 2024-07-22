import pyttsx3

engine = pyttsx3.init()

while True:
    user_input = input("enter anything else (or type 'stop'")
    if user_input.lower() == "stop":
        break
    engine.say(user_input)
    engine.runAndWait()

engine.stop()

