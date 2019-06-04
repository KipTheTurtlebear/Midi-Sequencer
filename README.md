# Midi-Sequencer
A midi sequencer with a basic GUI. Upload a .csv of MIDI messages through the GUI, and it will save a .mid file created from the .csv

To use, run the gui.py file, and then choose your .csv through the in-GUI file browser. Name you file, and then click convert. It will save a MIDI file
in the directory in which the gui.py file is located.

For an example of proper formatting for the .csv file, there is a test .csv. The order is COMMAND, CHANNEL, NOTE, VELOCITY, TIME. 

For messages that have different parameters than note_on/note_off, their first argument should be in the same location as the first argument in the list.