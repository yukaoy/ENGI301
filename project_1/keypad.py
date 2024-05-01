"""
--------------------------------------------------------------------------
KeyPad
--------------------------------------------------------------------------
License:   
Copyright 2021-2024 - Yuka Aoyama

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

KeyPad
A Keypad class manages instrument sounds and user interaction. It stores instrument sounds in a dictionary. Upon startup (boot(self)), it lights all keys for a brief welcome. When a key is pressed (handle_press(self)), the class plays the corresponding instrument sound and optionally allows recording. If recording is enabled (loop value is true), the key press intervals are saved and assigned as a new instrument to the bottom left key in the sound library.

"""
import time
import busio
from board import SCL, SDA
from adafruit_trellis import Trellis
from loop import Loop

import pygame

# Create the I2C interface
i2c = busio.I2C(SCL, SDA)

# Create a Trellis object for each board
trellis = Trellis(i2c) # 0x70 when no I2C address is supplied

# Dictionary to map buttons to sound files
sound_map = {
    0: "bass_1.wav", 
    1: "bass_2.wav",
    2: "bass_3.wav", 
    3: "snare_1.wav",
    4: "snare_2.wav", 
    5: "synth_1.wav",
    6: "synth_2.wav", 
    7: "hihat_1.wav",
    8: "loop_1.wav", 
    9: "voice_1.wav",
    10: "voice_2.wav", 
}
loop_button_pin = None
loop_variable = None
loop_dictionary = None
speaker = None
loop = Loop(loop_button_pin, loop_variable, loop_dictionary, speaker)

class Keypad():
    trellis = None
    def __init__(self, trellis):
        self.trellis = trellis
        pygame.init()
    
    def boot(self):
        # Light up all LEDs on boot
        self.trellis.led.fill(True)
    
    def handle_press(self):
        # Get a list of pressed buttons
        pressed_buttons = self.trellis.read_buttons()[0] #list[int]
         # Loop through pressed buttons and play sounds
        for button in pressed_buttons:
            if button in sound_map:
                sound_file = sound_map[button]
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
        if button == loop_button_pin:
            if self.loop_variable:
                loop.stop_loop()
            else:
                loop.start_loop()
    
    def save_recording(self, recording):
        sound_map.add(recording)
        

# Create a Keypad instance
keypad = Keypad(trellis)

# Boot up the keypad (turn on LEDs)
keypad.boot()

# Main loop to continuously check for button presses
while True:
    keypad.handle_press()
    time.sleep(0.1)  # Avoid rapid button presses              
    