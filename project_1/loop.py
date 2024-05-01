"""
--------------------------------------------------------------------------
Loop
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
The LoopButton class (Clear arcade button) controls recording behavior. It has two functions:

start_loop(self): This function listens for a button press. If pressed, it sets the internal loop value to true, enabling recording on subsequent key presses.

stop_loop(self): Similar to start_loop(self), it listens for a button press. When pressed, it sets the loop value to false, effectively stopping any ongoing recording.

"""
from threading import Thread
import time

class Loop:
    def __init__(self, button_pin, loop_variable, loop_dictionary, speaker):
        self.button_pin = button_pin
        self.loop_variable = loop_variable
        self.loop_dictionary = loop_dictionary  # Dictionary containing loop instruments and timings
        self.speaker = speaker
        self.thread = None
        self.is_looping = False

    def start_loop(self):
        if self.is_looping:
            return

        self.is_looping = True
        self.loop_variable = True
        
        def loop_thread():
            while self.is_looping:
                for instrument, interval in self.loop_dictionary.items():
                    self.speaker.play(instrument)
                    time.sleep(interval)

        self.thread = Thread(target=loop_thread)
        self.thread.start()

    def stop_loop(self):
        if not self.is_looping:
            return

        self.is_looping = False
        self.loop_variable = False

        if self.thread:
            self.thread.join()