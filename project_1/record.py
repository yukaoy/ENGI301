"""
--------------------------------------------------------------------------
Record
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

Record
The RecordButton class (Red arcade button) manages audio recording. It provides two functionalities:

start_record(self): This function listens for a button press. If pressed, it initiates recording using the USB microphone and flashes an LED to signal recording in progress.

stop_record(self): Upon a button press, this function stops the recording, saves it using the keypad's save_recording(recording) method, and turns off the LED.

"""
import threading
import sounddevice as sd
from keypad import Keypad

class Record:
    def __init__(self, button_pin, led_pin):
        self.button_pin = button_pin
        self.led_pin = led_pin
        self.recording = None
        self.is_recording = False
        self.thread = None
        self.keypad = Keypad()

    def start_record(self):
        if self.is_recording:
            return

        self.is_recording = True
        self.led_pin.value = True

        def record_audio():
            samplerate = 44100
            duration = 5  # seconds

            # Start recording in a separate thread
            self.recording = sd.rec(duration * samplerate, samplerate=samplerate, channels=1)
            sd.wait()
            self.is_recording = False
            self.led_pin.value = False

        self.thread = threading.Thread(target=record_audio)
        self.thread.start()

    def stop_record(self):
        if self.is_recording:
            self.thread.join()
            self.keypad.save_recording(self.recording)
            self.recording = None