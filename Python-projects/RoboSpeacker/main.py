import pyttsx3
if __name__ == '__main__':
    while True:
        print("Welcome to robospeaker 1.1")
        x = input("Enter what you want me to say: ")
        if (x=='q'):
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
