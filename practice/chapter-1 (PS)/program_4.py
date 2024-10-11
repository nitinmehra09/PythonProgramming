import pyttsx3

def text_to_speech(text):
    # Initialize the engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)
    
    # Wait until speech is finished
    engine.runAndWait()

# Example usage
text = "hi my name is nitin mehra"
text_to_speech(text)
