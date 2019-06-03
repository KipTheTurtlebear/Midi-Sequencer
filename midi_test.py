import mido
from tkinter import *
from mido import Message


def convertToMidi(event, filename, keynote):
    mid = mido.MidiFile(type=0)
    track = mido.MidiTrack()
    mid.tracks.append(track)

    track.append(mido.MetaMessage('time_signature'))
    track.append(mido.MetaMessage('key_signature', key=keynote))

    with open(filename, "r") as src:
        for line in src:
            command, channel, note, velocity, time = line.strip().split(",")
            msg = Message(command, note=int(note), velocity=int(velocity), time=int(time))
            track.append(msg)

    track.append(mido.MetaMessage('end_of_track'))

    name = input("Name this track: ")

    mid.save(name + '.mid')