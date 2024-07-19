import tkinter as tk
import time
from threading import Thread
import pygame

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
        
        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_breathing, font=("Helvetica", 18))
        self.start_button.pack(pady=20)
        
        # Time for each phase of the breathing cycle (in seconds)
        self.breath_in_time = 4
        self.hold_time = 4
        self.breath_out_time = 4
        
    def start_breathing(self):
        self.start_button.pack_forget()  # Hide the start button
        Thread(target=self.breathing_cycle).start()
    
    def breathing_cycle(self):
        while True:
            self.label.config(text="Breathe In")
            play_sound('breath_in.mp3')  # Play breathe in sound
            self.update_label("Breathe In", self.breath_in_time)
            
            self.label.config(text="Hold")
            play_sound('hold.mp3')  # Play hold sound
            self.update_label("Hold", self.hold_time)
            
            self.label.config(text="Breathe Out")
            play_sound('breath_out.mp3')  # Play breathe out sound
            self.update_label("Breathe Out", self.breath_out_time)
    
    def update_label(self, text, duration):
        for i in range(duration, 0, -1):
            self.label.config(text=f"{text}\n{i} seconds")
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = BreathingApp(root)
    root.mainloop()
