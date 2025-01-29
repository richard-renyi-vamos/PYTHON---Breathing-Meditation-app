from flask import Flask, render_template, jsonify
import pygame
import time
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Initialize Pygame mixer for sound
pygame.mixer.init()

# Function to play sound
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# The breathing cycle in a separate thread
def breathing_cycle():
    while True:
        update_phase("Breathe In", 'breath_in.mp3', 4)
        update_phase("Hold", 'hold.mp3', 4)
        update_phase("Breathe Out", 'breath_out.mp3', 4)

def update_phase(phase_text, sound_file, duration):
    # Update phase and play sound
    play_sound(sound_file)
    # Normally, you would use JavaScript for the timer and UI updates
    print(f"{phase_text} - {duration} seconds")

@app.route('/')
def index():
    return render_template("index.html")  # HTML to display UI

@app.route('/start')
def start_breathing():
    # Start breathing cycle in a separate thread
    Thread(target=breathing_cycle).start()
    return jsonify({"status": "Breathing started"})

@app.route('/stop')
def stop_breathing():
    # Here you can implement logic to stop the breathing cycle
    return jsonify({"status": "Breathing stopped"})

if __name__ == '__main__':
    app.run(debug=True)
