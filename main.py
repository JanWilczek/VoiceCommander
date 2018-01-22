#!/usr/bin/python

from tkinter import *
from tkinter import ttk
from CommandRecorder import CommandRecorder
from CommandRecognizer import recognize
from CommandHandler import CommandHandler
from auditok import ADSFactory, AudioEnergyValidator, StreamTokenizer, player_for
import wave, threading

def handle_command(filename):
    #state_label_text.set("Recognizing command")
    #root.update_idletasks()
    command, args = recognize(filename)
    # Here comes handling the recording in 'command.wav'
    if command != 'NO_MATCH':
        handler = CommandHandler()
        handler.handle(command, args)

def listen_for_commands(data, start, end):
    print("Acoustic activity at: {0}--{1}".format(start, end))
    if 'counter' not in listen_for_commands.__dict__:
            listen_for_commands.counter = 0
    #state_label_text.set("Command recorded")
    #root.update_idletasks()
    command_name = "command" + str(listen_for_commands.counter) + ".wav"
    save_file(command_name, data)
    threading.Thread(target=handle_command, args=(command_name,)).start()
    #state_label_text.set("Idle")
    #root.update_idletasks()
    listen_for_commands.counter += 1

def save_file(filename, data):
    wave_file = wave.open(filename, 'wb')
    wave_file.setnchannels(1)
    wave_file.setsampwidth(asource.get_sample_width())
    wave_file.setframerate(16000)
    wave_file.writeframes(b''.join(data))
    wave_file.close()

if __name__=="__main__":
    '''
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
    '''
    asource = ADSFactory.ads(sampling_rate=16000, sample_width=2, channels=1, frames_per_buffer=512, record=False, block_dur=0.01)

    validator = AudioEnergyValidator(sample_width=asource.get_sample_width(), energy_threshold=50)
    tokenizer = StreamTokenizer(validator=validator, min_length=100, max_length=500, max_continuous_silence=30)

    asource.open()

    tokenizer.tokenize(asource, callback=listen_for_commands)


    #root.mainloop()
