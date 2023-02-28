import speech_recognition as sr
import os
import keyboard

# Initialize the speech recognition engine as uncle google has instructed me
r = sr.Recognizer()

#Listen for a voice command
def listen_for_command():
    with sr.Microphone() as source:
        print("Say something bro")
        audio = r.listen(source)
    
    #recognize speech
    try:
        # Show_all not rly needed, trying to avoid some logs i don't need
        command = r.recognize_google(audio, show_all=False)
        print("You said: " + command)
        
        # If the command is "turn off the computer", execute the thging below
        if "turn off the computer" in command:
            os.system("shutdown /s /t 1")

        if "restart the computer" in command:
            os.system("shutdown /r /t 1")
    
    # Handle speech recognition errors
    except sr.UnknownValueError:
        print("Could not understand what are you saying")
    except sr.RequestError as e:
        print("RequestError logs; {0}".format(e))

# Define a function to start listening for voice commands when the key combination is pressed
def start_listening():
    keyboard.press_and_release('ctrl+shift+f')
    listen_for_command()

# Define a function to stop listening for voice commands when the key combination is released
# def stop_listening():
#     keyboard.press_and_release('ctrl+shift+f')
    
# Listen for key combination (Ctrl+Shift+F) to start listening for voice commands
keyboard.add_hotkey('ctrl+shift+f', start_listening, suppress=True, trigger_on_release=False)

# Wait for hotkeys to be pressed:)
keyboard.wait()
