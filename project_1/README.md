<h1>mini Instrument Controller</h1>

1. Keypad class
Dictionary of instrument sounds
boot(self)
- Light up all keys for 2 sec to indicate that the device is on
handle_press(self)
- Listen to the key press
- Play the corresponding instrument, speaker.play(instrument)
- If loop value is true, save the interval values in a list and set it to the dictionary
save_recording(self, recording)
- Add the recording as an instrument to the bottom left key in the instrument dictionary


2. Record button class (Red arcade button)
start_record(self)
- Listen to the button press
- Start recording using USB Mic
- Flash the LED to indicate that it is recording
stop_record(self)
- Listen to the button press
- Stop and save the recording, keypad.save_recording(recording).
- Turn off the LED


3. Loop button class (Clear arcade button)
start_loop(self)
- Listen to the button press
- Set loop value to true
stop_loop(self)
- Listen to the button press
- Set loop value to false


4. Speaker class
play(self, instrument)
- Play the input instrument once.
loop(self)
- For all instruments in the loop dictionary, iteratively call .play(instrument) with the set time intervals.


https://www.hackster.io/ya15/mini-instrument-controller-3ce008