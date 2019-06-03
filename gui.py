from tkinter import *
from tkinter import filedialog
import midi_test

root = Tk()
name = ""
KEYVALUES = ["A","A#m", "Ab", "Abm", "Am", "B", "Bb", "Bbm", "Bm", "C", "C#", "C#m", "Cb", "Cm", "D", "D#m", "Db", "Dm", "E", "Eb", "Ebm", "Em", "F", "F#", "F#m", "Fm", "G", "G#m", "Gb", "Gm"]
key_control = StringVar()
key_control.set(KEYVALUES[0])

root.title("MIDI Sequencer")


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
button2.grid(row=2)

# Key option menu
key = OptionMenu(root, key_control, *KEYVALUES)
key.grid(row=2, column=1)

# Convert to Midi button
button3 = Button(root, text="Convert")
button3.bind("<Button-1>", lambda event: midi_test.convertToMidi(event, name, key_control))
button3.grid(row=2, column=10)

# Quit Button
quitButton = Button(root, text="Quit", command=root.destroy)
quitButton.grid(row=2,column=24,sticky=E)
'''
label1 = Label(root, text="Name")
label2 = Label(root, text="Password")
check = Checkbutton(root, text="Keep me logged in")
entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, column=0, sticky=E)
label2.grid(row=1, column=0, sticky=E)
check.grid(columnspan=2)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
'''

'''
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=BOTTOM)
button4.pack(side=TOP)
'''

root.mainloop()

