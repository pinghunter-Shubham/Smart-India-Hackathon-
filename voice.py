import PySimpleGUI as sg
import pygame

# Initialize pygame
pygame.init()

# Function to play audio
def play_audio(audio_file):
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
    except pygame.error as e:
        sg.popup_error(f"Error loading audio: {str(e)}")

# Function to pause audio
def pause_audio():
    pygame.mixer.music.pause()

# Function to unpause audio
def unpause_audio():
    pygame.mixer.music.unpause()

# Function to stop audio
def stop_audio():
    pygame.mixer.music.stop()

# Function to get the audio file name from the user
def get_audio_file_name(filename):
    layout = [
        [sg.Button("Play"), sg.Button("Pause"), sg.Button("Unpause"), sg.Button("Stop")],
        [sg.Text("Status: Not playing", key="-STATUS-")]
    ]

    window = sg.Window("MP3 Audio Player", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Play":
            try:
                # Get the audio file name from the user
                mp3_file = filename

                if mp3_file:
                    # Play the audio
                    play_audio(mp3_file)

                    # Update status
                    window["-STATUS-"].update("Status: Playing")

                else:
                    sg.popup_error("Please select an audio file.")

            except Exception as e:
                sg.popup_error(f"Error: {str(e)}")
        elif event == "Pause":
            pause_audio()
        elif event == "Unpause":
            unpause_audio()
        elif event == "Stop":
            stop_audio()
            window["-STATUS-"].update("Status: Not playing")

    window.close()

# Call the function to get the audio file name from the user
# Clean up: Close pygame
pygame.mixer.quit()
