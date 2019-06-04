from tkinter import *
from tkinter import filedialog
import midi_test

root = Tk()
name = ""
KEYVALUES = ["A","A#m", "Ab", "Abm", "Am", "B", "Bb", "Bbm", "Bm", "C", "C#", "C#m", "Cb", "Cm", "D", "D#m", "Db", "Dm", "E", "Eb", "Ebm", "Em", "F", "F#", "F#m", "Fm", "G", "G#m", "Gb", "Gm"]
key_control = StringVar()
key_control.set(KEYVALUES[0])

root.title("MIDI Sequencer")


def onValidate(S):
    if S.isalnum():
        return True
    else:
        root.bell()
        return False


def printfilename(event):
    print(root.name)


def getfile(event):
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    entry.delete(0, END)
    entry.insert(0, filename)
    root.name = filename
    return filename


# Open File button
button1 = Button(root, text="Open File")
button1.bind("<Button-1>", getfile)
button1.grid(row=0)

# File path text box
entry = Entry(root, width=50, textvariable="file path")
entry.grid(row=0,column=1,padx=2,pady=2,sticky=W,columnspan=25)

# Only .csv warning
label1 = Label(root, text="Note: Only works with .csv files")
label1.grid(row=1)

# Print File path button 
button2 = Button(root, text="Print file path")
button2.bind("<Button-1>", printfilename)
button2.grid(row=4)

# Key option menu
key = OptionMenu(root, key_control, *KEYVALUES)
key.grid(row=3, column=1, sticky=W)

# Convert to Midi button
button3 = Button(root, text="Convert")
button3.bind("<Button-1>", lambda event: midi_test.convertToMidi(event, root.name, key_control.get(), entry1.get()))
button3.grid(row=4, column=10)

# Name Label
label2 = Label(root, text="Name of converted file:")
label2.grid(row=2)

# Name Entry
vcmd = (root.register(onValidate), '%S')
entry1 = Entry(root, validate="key", validatecommand=vcmd)
entry1.insert(END, 'myMIDI')
entry1.grid(row=2, column=1)

# Key Label
label3 = Label(root, text="Key of file:")
label3.grid(row=3)

# Quit Button
quitButton = Button(root, text="Quit", command=root.destroy)
quitButton.grid(row=4,column=24,sticky=E)

root.mainloop()

