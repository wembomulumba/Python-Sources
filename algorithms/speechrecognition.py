
#library for performing speech recognition, with support for several engines and APIs, online and offline.
#Speech recognition engine/API

#Quickstart: pip install SpeechRecognition. See the “Installing” section for more details.

#To quickly try it out, run python -m speech_recognition after installing.

import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
