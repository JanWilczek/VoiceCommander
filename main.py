#!/usr/bin/python

#import admin
from tkinter import *
from tkinter import ttk
from CommandRecorder import CommandRecorder
#from CommandHandler import CommandHandler

def record_and_handle_command():
    command_recorder.record_for_seconds("command" + str(listen_for_commands.counter) + ".wav")
    # Here comes handling the recording in 'command.wav'
    # (response/command, args) = ...
    # handler = CommandHandler()
    # handler.handle(command,args)

def listen_for_commands(event):
    if 'counter' not in listen_for_commands.__dict__:
            listen_for_commands.counter = 0
    state_label_text.set("Recording command...")
    root.update_idletasks()
    record_and_handle_command()
    state_label_text.set("Idle")
    root.update_idletasks()
    listen_for_commands.counter += 1

if __name__=="__main__":
    #if not admin.isUserAdmin():
    #    admin.runAsAdmin()
    command_recorder = CommandRecorder()

    root = Tk()
    root.title("VoiceCommander")

    frame = Frame(root, width=200, height=200)

    state_label_text = StringVar()
    state_label = Label(frame, textvariable=state_label_text)
    state_label.pack()
    state_label_text.set("Idle")

    recording_button = Button(frame, text="Record command")
    recording_button.bind("<Button-1>", listen_for_commands)
    recording_button.pack()

    frame.bind("<KeyRelease- >", listen_for_commands)

    frame.pack()
    frame.focus_set()
    root.mainloop()
