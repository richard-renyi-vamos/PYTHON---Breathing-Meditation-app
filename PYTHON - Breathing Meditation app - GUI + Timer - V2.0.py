import tkinter as tk
from threading import Thread
import pygame
import time

# Initialize Pygame mixer for sound
pygame.mixer.init()

# Function to play sound
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

class BreathingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Breathing Meditation App")
        
        # Create and place the label for instructions
        self.label = tk.Label(root, text="Welcome to Breathing Meditation", font=("Helvetica", 24))
        self.label.pack(pady=20)
        
        # Timer label
        self.timer_label = tk.Label(root, text="", font=("Helvetica", 20))
        self.timer_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_breathing, font=("Helvetica", 18))
        self.start_button.pack(pady=20)
        
        # Time for each phase of the breathing cycle (in seconds)
        self.breath_in_time = 4
        self.hold_time = 4
        self.breath_out_time = 4
        
        # State variable for running the breathing cycle
        self.running = False

    def start_breathing(self):
        self.start_button.pack_forget()  # Hide the start button
        self.running = True
        Thread(target=self.breathing_cycle).start()

    def breathing_cycle(self):
        while self.running:
            self.update_phase("Breathe In", 'breath_in.mp3', self.breath_in_time)
            self.update_phase("Hold", 'hold.mp3', self.hold_time)
            self.update_phase("Breathe Out", 'breath_out.mp3', self.breath_out_time)

    def update_phase(self, text, sound_file, duration):
        self.label.config(text=text)
        play_sound(sound_file)

        for i in range(duration, 0, -1):
            if not self.running:
                break
            self.timer_label.config(text=f"{i} seconds")
            time.sleep(1)

    def stop_breathing(self):
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = BreathingApp(root)

    # Adding a Quit button
    quit_button = tk.Button(root, text="Quit", command=root.destroy, font=("Helvetica", 18))
    quit_button.pack(pady=20)

    root.mainloop()
