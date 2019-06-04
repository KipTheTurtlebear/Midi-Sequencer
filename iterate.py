from mido import MidiFile
import sys


mid = MidiFile(sys.argv[1])

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)