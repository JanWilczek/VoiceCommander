from auditok import ADSFactory, AudioEnergyValidator, StreamTokenizer, player_for
import wave


def echo(data, start, end):
    print("Acoustic activity at: {0}--{1}".format(start, end))
    wave_file = wave.open("test.wav", 'wb')
    wave_file.setnchannels(1)
    wave_file.setsampwidth(asource.get_sample_width())
    wave_file.setframerate(16000)
    wave_file.writeframes(b''.join(data))
    wave_file.close()


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
tokenizer = StreamTokenizer(validator=validator, min_length=100, max_continuous_silence=500)

asource.open()

tokenizer.tokenize(asource, callback=echo)
