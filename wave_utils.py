import wave


def save_wave_file(filename, data, samplerate=16000, channels=1, sample_width=2):
    wave_file = wave.open(filename, 'wb')
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(sample_width)
    wave_file.setframerate(samplerate)
    wave_file.writeframes(b''.join(data))
    wave_file.close()

