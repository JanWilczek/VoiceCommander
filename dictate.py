from imports.techmo_dictation_pathfinder_pyclients.audio_provider import get_audio
from imports.techmo_dictation_pathfinder_pyclients.dictation_client import DictationClient
from address_provider import AddressProvider
from logger import log, error_log
import grpc


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

