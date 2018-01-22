#!/usr/bin/env python
# -*- coding: utf-8 -*-

from imports.techmo_sarmata_pyclient.utils.wave_loader import load_wave
from imports.techmo_sarmata_pyclient.service.sarmata_settings import SarmataSettings
from imports.techmo_sarmata_pyclient.service.sarmata_recognize import SarmataRecognizer
from imports.techmo_sarmata_pyclient.service.asr_service_pb2 import ResponseStatus
from address_provider import AddressProvider
import os


def print_results(responses):
    if responses is None:
        print("Empty results - None object")
        return

    for response in responses:
        if response is None:
            print("Empty results - skipping response")
            continue

        print("Received response with status: {}".format(ResponseStatus.Name(response.status)))

        if response.error:
            print("[ERROR]: {}".format(response.error))

        for n, res in enumerate(response.results):
            transcript = " ".join([word.transcript for word in res.words])
            print("[{}.] {} /{}/ ({})".format(n, transcript, res.semantic_interpretation, res.confidence))

def print_again(responses):
    info = ["NO_MATCH", 0]
    confidence = 0
    if responses is None:
        print("Empty results - None object")
        return info

    for response in responses:
        if response is None:
            print("Empty results - skipping response")
            continue
        if ResponseStatus.Name(response.status) == "NO_MATCH":
            return info
        if response.error:
            print("[ERROR]: {}".format(response.error))

        for n, res in enumerate(response.results):
            if res.confidence > confidence:
                confidence = res.confidence
                info[0] = res.semantic_interpretation
    info[1] = confidence
    return info

def recognize(filename):
    ap = AddressProvider()
    wave_file = filename
    grammar_file = "Grammatic_Frames/Command_structure.abnf"
    address = ap.get("sarmata")

    audio = load_wave(wave_file)

    settings = SarmataSettings()
    session_id = os.path.basename(wave_file)
    settings.set_session_id(session_id)
    settings.load_grammar(grammar_file)
    recognizer = SarmataRecognizer(address)
    results = recognizer.recognize(audio, settings)

    tmp = print_again(results)
    semantic = tmp[0]
    print(semantic + " :Sarmata ")

    result = semantic.split(" ")
    if len(result) == 1:
        return result[0], None
    else:
        return result[0], result[1]
