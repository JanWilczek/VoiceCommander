import pyaudio
import wave



class CommandRecorder:

    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

    def record_for_seconds(self, filename="command.wav", record_seconds=5):
        audio = pyaudio.PyAudio()

        # start Recording
        stream = audio.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE, input=True,
                            frames_per_buffer=self.CHUNK)
        print("recording...")
        frames = []

        if record_seconds > 0:
            for i in range(0, int(self.RATE / self.CHUNK * record_seconds)):
                data = stream.read(self.CHUNK)
                frames.append(data)
        else:   # dictation recording
            try:
                while True:
                    data = stream.read(self.CHUNK)
                    frames.append(data)
            except KeyboardInterrupt:
                pass

        print("finished recording")

        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(filename, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
