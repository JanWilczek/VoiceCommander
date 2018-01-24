import pyaudio
from wave_utils import save_wave_file


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

        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        save_wave_file(filename, frames, channels=self.CHANNELS, sample_width=audio.get_sample_size(self.FORMAT), samplerate=self.RATE)

