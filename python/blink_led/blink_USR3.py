# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Blink USR3
--------------------------------------------------------------------------
License:   
Copyright 2024 - Yuka Aoyama

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Blinks the USR3 LED on PocketBeagle at 5 Hz (i.e. 5 full on/off cycles per second)
using the Adafruit_BBIO library.

--------------------------------------------------------------------------
"""
# ------------------------------------------------------------------------
# Import Statements
# ------------------------------------------------------------------------
import Adafruit_BBIO.GPIO as GPIO
import time

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------
USR3_LED = "USR3"

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------
def blink_led():
    """ 
    Blinks the USR 3 LED at 5Hz
    """
    try: 
        # Set up LED
        GPIO.setup(USR3_LED, GPIO.OUT)

        # Simulate blink by setting GPIO.HIGH and GPIO.LOW in turn continuously. 
        # 0.1s intervals for 5Hz
        while True:
            GPIO.output(USR3_LED, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(USR3_LED, GPIO.LOW)
            time.sleep(0.1)

    except:
        GPIO.cleanup()

if __name__ == "__main__":
    blink_led()