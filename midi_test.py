import sys
import mido
from mido import Message


mid = mido.MidiFile(type=0)
track = mido.MidiTrack()
mid.tracks.append(track)


key_note = input("What is the key?")
#    if key_note in ['A' 'A#m' 'Ab' 'Abm' 'Am' 'B' 'Bb' 'Bbm' 'Bm' 'C' 'C#' 'C#m'
#    'Cb' 'Cm' 'D' 'D#m' 'Db' 'Dm' 'E' 'Eb' 'Ebm' 'Em' 'F' 'F#' 'F#m' 'Fm' 'G' 'G#m' 'Gb' 'Gm']:
#        break

track.append(mido.MetaMessage('time_signature'))
track.append(mido.MetaMessage('key_signature', key=key_note))

with open(sys.argv[1], "r") as src:
    for line in src:
        command, channel, note, velocity, time = line.strip().split(",")
        msg = Message(command, note=int(note), velocity=int(velocity), time=int(time))
        track.append(msg)

track.append(mido.MetaMessage('end_of_track'))

name = input("Name this track: ")

mid.save(name + '.mid')