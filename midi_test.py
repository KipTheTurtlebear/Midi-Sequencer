import mido
from tkinter import *
from mido import Message


def convertToMidi(event, filename, keynote, saveName):
    mid = mido.MidiFile(type=0)
    track = mido.MidiTrack()
    mid.tracks.append(track)

    track.append(mido.MetaMessage('time_signature'))
    track.append(mido.MetaMessage('key_signature', key=keynote))

    print("Filename: " + filename)

    with open(filename, "r") as src:
        for line in src:
            command, channel, note, velocity, time = line.strip().split(",")
            if command == 'note_on' or command == 'note_off':
                msg = Message(command, channel=int(channel), note=int(note), velocity=int(velocity), time=int(time))
            elif command == 'polytouch':
                msg = Message(command, channel=int(channel), note=int(note), value=int(velocity))
            elif command == 'control_change':
                msg = Message(command, channel=int(channel), control=int(note), value=int(velocity))
            elif command == 'program_change':
                msg = Message(command, channel=int(channel), program=int(note))
            elif command == 'aftertouch':
                msg = Message(command, channel=int(channel), value=int(note))
            elif command == 'pitchwheel':
                msg = Message(command, channel=int(channel), pitch=int(note))
            elif command == 'sysex':
                msg = Message(command, data=int(channel))
            track.append(msg)

    track.append(mido.MetaMessage('end_of_track'))

    mid.save(saveName + '.mid')