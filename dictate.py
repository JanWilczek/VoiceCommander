from auditok import ADSFactory, AudioEnergyValidator, StreamTokenizer
from imports.techmo_dictation_pathfinder_pyclients.audio_provider import get_audio
from imports.techmo_dictation_pathfinder_pyclients.dictation_client import DictationClient
from address_provider import AddressProvider
from logger import log, error_log
from wave_utils import save_wave_file
import grpc


def begin_dictation():

    def end_dictation(data, start, end):
        asource.close()
        log("Dictation ended.")
        save_wave_file(filename, data, samplerate=asource.get_sampling_rate(),
                       sample_width=asource.get_sample_width(), channels=asource.get_channels())

    filename = "dictation.wav"
    asource = ADSFactory.ads(sampling_rate=44100, sample_width=4, channels=1, frames_per_buffer=1024, record=False,
                             block_dur=0.05)
    validator = AudioEnergyValidator(sample_width=asource.get_sample_width(), energy_threshold=60)
    tokenizer = StreamTokenizer(validator=validator, min_length=100, max_length=400, max_continuous_silence=60)

    asource.open()
    log("Dictation started.")
    tokenizer.tokenize(asource, callback=end_dictation)     # No possibility of stopping the tokenizer
    return filename


def interpret_dication(wave_filepath):
    ap = AddressProvider()
    address = ap.get("dictation")
    dc = DictationClient(address)

    # Read wave file
    audio = get_audio(wave_filepath)

    # Run Pathfinder
    try:
        results = dc.recognize(method="sync", audio=audio)
    except grpc.RpcError as e:
        error_log("[Server-side error] Received following RPC error from the Pathfinder service:", str(e))
        import sys
        sys.exit(1)

    transcription = ""
    for idx, response in enumerate(results):
        if not len(response):
            log("No phrases detected.")
        else:
            transcription += "\"{}\"".format(response['transcript'])
    return transcription