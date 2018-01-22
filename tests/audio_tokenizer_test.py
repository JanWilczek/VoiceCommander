from auditok import ADSFactory, AudioEnergyValidator, StreamTokenizer, player_for
import wave

def echo(data, start, end):
   print("Acoustic activity at: {0}--{1}".format(start, end))
   waveFile = wave.open("test.wav", 'wb')
   waveFile.setnchannels(1)
   waveFile.setsampwidth(asource.get_sample_width())
   waveFile.setframerate(16000)
   waveFile.writeframes(b''.join(data))
   waveFile.close()
   #player.play(''.join(data))

'''
# record = True so that we'll be able to rewind the source.
# max_time = 10: read 10 seconds from the microphone
asource = ADSFactory.ads(record=True)

validator = AudioEnergyValidator(sample_width=asource.get_sample_width(), energy_threshold=50)
tokenizer = StreamTokenizer(validator=validator, min_length=20, max_length=250, max_continuous_silence=30)

player = player_for(asource)
asource.open()

tokenizer.tokenize(asource, callback=echo)
'''
asource = ADSFactory.ads(sampling_rate=16000, sample_width=2, channels=1, frames_per_buffer=128, record=False,
                         block_dur=0.01)

validator = AudioEnergyValidator(sample_width=asource.get_sample_width(), energy_threshold=50)
tokenizer = StreamTokenizer(validator=validator, min_length=100, max_length=500, max_continuous_silence=30)

asource.open()

tokenizer.tokenize(asource, callback=echo)
